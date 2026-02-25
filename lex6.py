import re

file = open("input.c", "r")
code = file.read()

patterns = {
    "KEYWORD": r'\b(int|float|if|else|while|return)\b',
    "NUMBER": r'\b\d+(\.\d+)?\b',
    "IDENTIFIER": r'\b[a-zA-Z_]\w*\b',
    "OPERATOR": r'[+\-*/=]',
    "SYMBOL": r'[();{}]'
}

print("Token Table\n-------------")

for token_type, pattern in patterns.items():
    for match in re.finditer(pattern, code):
        print(match.group(), "->", token_type)
