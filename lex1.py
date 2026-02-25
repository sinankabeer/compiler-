import re
KEYWORDS = {"if", "else", "while", "int", "float", "return"}
OPERATORS = {"+", "-", "*", "/", "=", "==", "<", ">", "<=", ">="}
SEPARATORS = {"(", ")", "{", "}", ";", ","}

def lexical_analyzer(code):
    tokens = re.findall(r'\w+|==|<=|>=|[+\-*/=<>(){};,]', code)

    for token in tokens:
        if token in KEYWORDS:
            print(f"{token} : KEYWORD")
        elif token in OPERATORS:
            print(f"{token} : OP")
        elif token in SEPARATORS:
            print(f"{token} : SEPARATOR")
        elif token.isdigit():
            print(f"{token} : NUMBER")
        else:
            print(f"{token} : IDENTIFIER")
code = "int a = b + 10;"
lexical_analyzer(code)
