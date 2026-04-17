from dataclasses import dataclass
from typing import List, Set, FrozenSet, Dict

@dataclass(frozen=True)
class Item:
    lhs: str
    rhs: str
    dot_pos: int

class LR0:
    def __init__(self, grammar: Dict[str, List[str]], start_symbol: str):
        self.grammar = grammar
        self.grammar[start_symbol + "'"] = [start_symbol]
        self.start = start_symbol + "'"

    def closure(self, items: Set[Item]) -> FrozenSet[Item]:
        closure_set = set(items)
        changed = True
        while changed:
            new_items = set()
            for item in closure_set:
                if item.dot_pos < len(item.rhs):
                    next_sym = item.rhs[item.dot_pos]
                    if next_sym.isupper():
                        for prod in self.grammar.get(next_sym, []):
                            new_items.add(Item(next_sym, prod, 0))
            if new_items.issubset(closure_set): changed = False
            else: closure_set.update(new_items)
        return frozenset(closure_set)

    def goto(self, items: FrozenSet[Item], symbol: str) -> FrozenSet[Item]:
        moved = set()
        for item in items:
            if item.dot_pos < len(item.rhs) and item.rhs[item.dot_pos] == symbol:
                moved.add(Item(item.lhs, item.rhs, item.dot_pos + 1))
        return self.closure(moved)

if __name__ == '__main__':
    lr0 = LR0({'E': ['E+T', 'T'], 'T': ['id']}, 'E')
    i0 = lr0.closure({Item("E'", "E", 0)})
    print("I0:", i0)
