from collections import defaultdict
from typing import Dict, List, Set

class OperatorPrecedenceSets:
    def __init__(self, grammar: Dict[str, List[str]]):
        self.grammar = grammar
        self.leading: Dict[str, Set[str]] = defaultdict(set)
        self.trailing: Dict[str, Set[str]] = defaultdict(set)
        self.compute_leading()
        self.compute_trailing()

    def compute_leading(self):
        changed = True
        while changed:
            changed = False
            for lhs, rhs_list in self.grammar.items():
                before = len(self.leading[lhs])
                for rhs in rhs_list:
                    if len(rhs) > 0 and not rhs[0].isupper():
                        self.leading[lhs].add(rhs[0])
                    elif len(rhs) > 0 and rhs[0].isupper():
                        self.leading[lhs].update(self.leading[rhs[0]])
                        if len(rhs) > 1 and not rhs[1].isupper():
                            self.leading[lhs].add(rhs[1])
                if len(self.leading[lhs]) > before: changed = True

    def compute_trailing(self):
        changed = True
        while changed:
            changed = False
            for lhs, rhs_list in self.grammar.items():
                before = len(self.trailing[lhs])
                for rhs in rhs_list:
                    if len(rhs) > 0 and not rhs[-1].isupper():
                        self.trailing[lhs].add(rhs[-1])
                    elif len(rhs) > 0 and rhs[-1].isupper():
                        self.trailing[lhs].update(self.trailing[rhs[-1]])
                        if len(rhs) > 1 and not rhs[-2].isupper():
                            self.trailing[lhs].add(rhs[-2])
                if len(self.trailing[lhs]) > before: changed = True

if __name__ == '__main__':
    op = OperatorPrecedenceSets({'E': ['E+T', 'T'], 'T': ['T*F', 'F'], 'F': ['(E)', 'id']})
    print("LEADING:", dict(op.leading))
    print("TRAILING:", dict(op.trailing))
