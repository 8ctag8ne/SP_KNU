from Lexer import AssemblerLexer
test_code = """
.MODEL SMALL        ; це модель програми
.STACK 100h        

.DATA
message DB 'Hello, World!'  ; повідомлення
number  DW 42      

.CODE
start:             
    MOV AX, @DATA  
    MOV DS, AX     

    MOV DX, [BX+5] 
    INT 21h        
    """

lexer = AssemblerLexer()
print("Кольоровий вивід:")
lexer.print_colored_code(test_code)
print("\nСписок лексем:")
lexer.print_token_pairs(test_code)