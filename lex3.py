import re
code = """
int a = 10;
float b = 20.5;
if(a >= b){
    return "Hello";
}
// comment line
"""

token_specification = [
    ('COMMENT',   r'//.*'),                     
    ('STRING',    r'"[^"]*"'),                  
    ('KEYWORD',   r'\b(int|float|if|else|while|return)\b'),
    ('NUMBER',    r'\b\d+(\.\d+)?\b'),          
    ('OPERATOR',  r'==|!=|>=|<=|[+\-*/=><]'),
    ('SYMBOL',    r'[(){};,]'),
    ('IDENTIFIER',r'\b[a-zA-Z_]\w*\b'),
    ('SKIP',      r'[ \t\n]+'),                 
    ('MISMATCH',  r'.')                         
]

tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)

print("Token Table\n-----------")

for match in re.finditer(tok_regex, code):
    kind = match.lastgroup
    value = match.group()

    if kind == 'SKIP' or kind == 'COMMENT':
        continue
    elif kind == 'MISMATCH':
        print(value, "-> Unknown")
    else:
        print(value, "->", kind)
