import re

keywords = {"int", "float", "if", "else", "while", "return"}

token_pattern = re.compile(
    r'\b\d+\.\d+\b|'      # float
    r'\b\d+\b|'           # int
    r'\b[a-zA-Z_]\w*\b|'  # identifier
    r'[+\-*/=><]+|'       # operator
    r'[(){};,]'           # symbol
)

code = """
int a = 10;
float b = 5.2;
if(a>b){
    return a;
}
"""

print("Line  Token   Type")
print("----------------------")

for line_no, line in enumerate(code.split('\n'), start=1):
    for token in token_pattern.findall(line):

        if token in keywords:
            ttype = "KEYWORD"
        elif token.replace('.', '', 1).isdigit():
            ttype = "NUMBER"
        elif token in "+-*/=><":
            ttype = "OPERATOR"
        elif token in "(){};,":
            ttype = "SYMBOL"
        else:
            ttype = "IDENTIFIER"

        print(f"{line_no:<5} {token:<7} {ttype}")
