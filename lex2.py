keywords = {"int", "float", "if", "else", "while", "return"}
operators = {"+", "-", "*", "/", "=", ">", "<"}
symbols = {"(", ")", "{", "}", ";", ","}

code = input("Enter code line: ")

tokens = code.split()

for token in tokens:
    if token in keywords:
        print(token, "-> Keyword")

    elif token in operators:
        print(token, "-> Operator")

    elif token in symbols:
        print(token, "-> Symbol")

    elif token.isdigit():
        print(token, "-> Number")

    elif token.isidentifier():
        print(token, "-> Identifier")

    else:
        print(token, "-> Unknown")
