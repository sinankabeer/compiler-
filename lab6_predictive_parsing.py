from typing import Dict, List
from lab5_first_follow import FirstFollow

class PredictiveParser:
    def __init__(self, grammar: Dict[str, List[str]], start_symbol: str):
        self.grammar = grammar
        self.ff = FirstFollow(grammar, start_symbol)
        self.table = {}
        self.build_table()

    def build_table(self):
        for non_term, productions in self.grammar.items():
            self.table[non_term] = {}
            for prod in productions:
                first_alpha = self._get_first_of_string(prod)
                for terminal in first_alpha - {'ε'}:
                    self.table[non_term][terminal] = prod
                if 'ε' in first_alpha:
                    for terminal in self.ff.follow[non_term]:
                        self.table[non_term][terminal] = prod

    def _get_first_of_string(self, string: str) -> set:
        if string == 'ε': return {'ε'}
        res = set()
        for char in string:
            f = self.ff.first[char] if char.isupper() else {char}
            res.update(f - {'ε'})
            if 'ε' not in f: break
        else: res.add('ε')
        return res

if __name__ == '__main__':
    parser = PredictiveParser({'S': ['aABb'], 'A': ['c', 'ε'], 'B': ['d']}, 'S')
    print("Parse Table:", parser.table)
