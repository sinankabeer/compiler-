import re

keywords = {"int", "float", "if", "else", "while", "return"}
symbol_table = {}

code = "int a = 10; float b = a + 5;"

tokens = re.findall(r'\b\w+\b|[+\-*/=;]', code)

print("Tokens\n-------")

for token in tokens:
    if token in keywords:
        print(token, "-> KEYWORD")

    elif token.isdigit():
        print(token, "-> NUMBER")

    elif token in "+-*/=":
        print(token, "-> OPERATOR")

    elif token == ";":
        print(token, "-> SYMBOL")

    else:
        print(token, "-> IDENTIFIER")

        if token not in symbol_table:
            symbol_table[token] = len(symbol_table) + 1


print("\nSymbol Table\n-------------")
for name, idx in symbol_table.items():
    print(idx, name)
