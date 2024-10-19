from enum import Enum

class TokenType(Enum):
    LABEL = 'LABEL'
    INSTRUCTION = 'INSTRUCTION'
    REGISTER = 'REGISTER'
    NUMBER = 'NUMBER'
    DIRECTIVE = 'DIRECTIVE'
    OPERATOR = 'OPERATOR'
    COMMENT = 'COMMENT'
    STRING = 'STRING'
    IDENTIFIER = 'IDENTIFIER'
    ERROR = 'ERROR'
    WHITESPACE = 'WHITESPACE'


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value