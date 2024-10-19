import re
from Tokens import Token, TokenType
from assembler_patterns import ASSEMBLER_PATTERNS

class AssemblerLexer:
    def __init__(self):
        self.patterns = [(re.compile(p), t) for p, t in ASSEMBLER_PATTERNS]

        # Кольори для різних типів лексем
        self.colors = {
            TokenType.LABEL: '\033[95m',  # магента
            TokenType.INSTRUCTION: '\033[94m',  # синій
            TokenType.REGISTER: '\033[92m',  # зелений
            TokenType.NUMBER: '\033[93m',  # жовтий
            TokenType.DIRECTIVE: '\033[96m',  # блакитний
            TokenType.OPERATOR: '\033[91m',  # червоний
            TokenType.COMMENT: '\033[90m',  # сірий
            TokenType.STRING: '\033[93m',  # жовтий
            TokenType.IDENTIFIER: '\033[97m',  # білий
            TokenType.ERROR: '\033[41m',  # червоний фон
            TokenType.WHITESPACE: '\033[0m',
        }
        self.RESET = '\033[0m'

    def tokenize(self, code):
        tokens = []
        lines = code.split('\n')

        for line in lines:
            position = 0

            while position < len(line):
                match = None
                for pattern, token_type in self.patterns:
                    regex_match = pattern.match(line, position)
                    if regex_match:
                        value = regex_match.group()
                        match = Token(token_type, value)
                        position = regex_match.end()
                        break

                if match:
                    tokens.append(match)
                else:
                    # Зберігаємо пробіли
                    if position < len(line) and line[position].isspace():
                        tokens.append(Token(TokenType.WHITESPACE, " "))
                        position += 1
                    else:
                        # Нерозпізнаний символ - помилка
                        if position < len(line):
                            error_token = Token(TokenType.ERROR, line[position])
                            tokens.append(error_token)
                            position += 1

            tokens.append(Token(None, '\n'))

        return tokens

    def print_colored_code(self, code):
        tokens = self.tokenize(code)
        for token in tokens:
            if token.type is None:  # Перенос рядка
                print()
            else:
                print(f"{self.colors[token.type]}{token.value}{self.RESET}", end='')

        print("\n\nЛегенда:")
        used_types = set(token.type for token in tokens if token.type is not None)
        all_types = {
                    TokenType.LABEL: "LABEL",
                    TokenType.INSTRUCTION: "INSTRUCTION",
                    TokenType.REGISTER: "REGISTER",
                    TokenType.NUMBER: "NUMBER",
                    TokenType.DIRECTIVE: "DIRECTIVE",
                    TokenType.OPERATOR: "OPERATOR",
                    TokenType.COMMENT: "COMMENT",
                    TokenType.STRING: "STRING",
                    TokenType.IDENTIFIER: "IDENTIFIER",
                    TokenType.ERROR: "ERROR"
                }
        for token_type in TokenType:
            if token_type in used_types and token_type != TokenType.WHITESPACE:
                example_text = all_types[token_type]
                print(f"{self.colors[token_type]}{example_text}{self.RESET}")

    def print_token_pairs(self, code):
        tokens = self.tokenize(code)
        for token in tokens:
            if token.type and token.type != TokenType.WHITESPACE:  # Пропускаємо токени переносу рядка
                print(f"<{token.value}, {token.type.value}>")
