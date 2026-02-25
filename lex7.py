import re

def analyze(code):
    tokens = re.findall(r'\b\w+\b|[^\s]', code)

    for t in tokens:
        if t in {"int","float","if","else","return"}:
            print(t,"-> KEYWORD")
        elif t.isdigit():
            print(t,"-> NUMBER")
        elif t.isidentifier():
            print(t,"-> IDENTIFIER")
        elif t in "+-*/=":
            print(t,"-> OPERATOR")
        else:
            print(t,"-> SYMBOL")


print("1. Manual Input")
print("2. File Input")

choice = input("Choice: ")

if choice == "1":
    code = input("Enter code: ")
else:
    with open("input.c") as f:
        code = f.read()

analyze(code)
