from typing import Dict, Set, List
from collections import defaultdict

class FirstFollow:
    def __init__(self, grammar: Dict[str, List[str]], start_symbol: str):
        self.grammar = grammar
        self.start = start_symbol
        self.first: Dict[str, Set[str]] = defaultdict(set)
        self.follow: Dict[str, Set[str]] = defaultdict(set)
        self.compute_first()
        self.compute_follow()

    def compute_first(self):
        def first_of(symbol: str) -> Set[str]:
            if not symbol.isupper(): return {symbol}
            res = set()
            for prod in self.grammar[symbol]:
                if prod == 'ε': res.add('ε')
                else:
                    for char in prod:
                        f = first_of(char)
                        res.update(f - {'ε'})
                        if 'ε' not in f: break
                    else: res.add('ε')
            return res

        for non_term in self.grammar:
            self.first[non_term] = first_of(non_term)

    def compute_follow(self):
        self.follow[self.start].add('$')
        changed = True
        while changed:
            changed = False
            for head, productions in self.grammar.items():
                for prod in productions:
                    for i, symbol in enumerate(prod):
                        if symbol.isupper():
                            before = len(self.follow[symbol])
                            if i + 1 < len(prod):
                                next_first = self.first[prod[i+1]]
                                self.follow[symbol].update(next_first - {'ε'})
                                if 'ε' in next_first:
                                    self.follow[symbol].update(self.follow[head])
                            else:
                                self.follow[symbol].update(self.follow[head])
                            if len(self.follow[symbol]) > before:
                                changed = True

if __name__ == '__main__':
    ff = FirstFollow({'S': ['aABb'], 'A': ['c', 'ε'], 'B': ['d']}, 'S')
    print("FIRST:", dict(ff.first))
    print("FOLLOW:", dict(ff.follow))
