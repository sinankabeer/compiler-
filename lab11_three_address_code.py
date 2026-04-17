from dataclasses import dataclass
from typing import List, Optional

@dataclass
class TAC:
    op: str
    arg1: str
    arg2: Optional[str]
    result: str

class TACRepresentations:
    def __init__(self, code: List[TAC]):
        self.code = code

    def print_quadruple(self):
        print(f"{'OP':<6} {'ARG1':<6} {'ARG2':<6} {'RESULT':<6}")
        for c in self.code:
            print(f"{c.op:<6} {c.arg1:<6} {str(c.arg2):<6} {c.result:<6}")

    def print_triple(self):
        print(f"{'ID':<4} {'OP':<6} {'ARG1':<6} {'ARG2':<6}")
        for i, c in enumerate(self.code):
            arg1 = f"({self._find_res(c.arg1)})" if self._is_temp(c.arg1) else c.arg1
            arg2 = f"({self._find_res(c.arg2)})" if self._is_temp(c.arg2) else str(c.arg2)
            print(f"({i:<2}) {c.op:<6} {arg1:<6} {arg2:<6}")

    def _is_temp(self, var) -> bool:
        return bool(var and str(var).startswith('t'))

    def _find_res(self, res) -> int:
        for i, c in enumerate(self.code):
            if c.result == res: return i
        return -1

if __name__ == '__main__':
    # t1 = b * c; t2 = a + t1
    tacs = [TAC('*', 'b', 'c', 't1'), TAC('+', 'a', 't1', 't2')]
    rep = TACRepresentations(tacs)
    print("Quadruples:")
    rep.print_quadruple()
    print("\nTriples:")
    rep.print_triple()
