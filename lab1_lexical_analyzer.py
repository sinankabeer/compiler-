import re
from typing import NamedTuple, Iterable

class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int

class LexicalAnalyzer:
    def __init__(self):
        # Advanced: Order matters. Keywords must come before general identifiers.
        self.rules = [
            ('COMMENT', r'//.*|/\*[\s\S]*?\*/'),
            ('KEYWORD', r'\b(if|else|while|return|int|float|void)\b'),
            ('ID', r'[a-zA-Z_]\w*'),
            ('FLOAT', r'\d+\.\d+'),
            ('INT', r'\d+'),
            ('OP', r'[+\-*/%=<>!&|]+'),
            ('PUNC', r'[;,\{\}\(\)\[\]]'),
            ('SPACE', r'[ \t]+'),
            ('NEWLINE', r'\n'),
            ('MISMATCH', r'.')
        ]
        self.regex = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.rules))

    def tokenize(self, code: str) -> Iterable[Token]:
        line_num = 1
        line_start = 0
        for match in self.regex.finditer(code):
            kind = match.lastgroup
            value = match.group()
            column = match.start() - line_start
            
            if kind == 'NEWLINE':
                line_start = match.end()
                line_num += 1
            elif kind == 'SPACE' or kind == 'COMMENT':
                continue
            elif kind == 'MISMATCH':
                raise RuntimeError(f'Unexpected character {value!r} at line {line_num}')
            else:
                yield Token(kind, value, line_num, column)

if __name__ == '__main__':
    lexer = LexicalAnalyzer()
    code = "int main() { return 0; }"
    for token in lexer.tokenize(code):
        print(token)
