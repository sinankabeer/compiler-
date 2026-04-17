from typing import List
from lab11_three_address_code import TAC

class SimpleCodeGenerator:
    def __init__(self):
        self.registers = {'R0': None, 'R1': None}

    def get_reg(self, var: str) -> str:
        for reg, val in self.registers.items():
            if val == var: return reg
        for reg, val in self.registers.items():
            if val is None:
                self.registers[reg] = var
                return reg
        return 'R0' # Fallback primitive register spill

    def generate(self, tacs: List[TAC]):
        for tac in tacs:
            reg1 = self.get_reg(tac.arg1)
            print(f"MOV {tac.arg1}, {reg1}")
            if tac.arg2:
                reg2 = self.get_reg(tac.arg2)
                if self.registers[reg2] != tac.arg2:
                    print(f"MOV {tac.arg2}, {reg2}")
                
                op_map = {'+': 'ADD', '-': 'SUB', '*': 'MUL', '/': 'DIV'}
                print(f"{op_map[tac.op]} {reg2}, {reg1}")
            self.registers[reg1] = tac.result
            print(f"MOV {reg1}, {tac.result}")

if __name__ == '__main__':
    tacs = [TAC('*', 'b', 'c', 't1'), TAC('+', 'a', 't1', 't2')]
    cg = SimpleCodeGenerator()
    cg.generate(tacs)
