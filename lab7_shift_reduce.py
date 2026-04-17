from typing import List, Tuple

class ShiftReduceParser:
    def __init__(self, grammar_rules: List[Tuple[str, str]]):
        self.rules = grammar_rules

    def parse(self, tokens: List[str]):
        stack = []
        buffer = tokens + ['$']
        
        print(f"{'STACK':<20} | {'BUFFER':<20} | {'ACTION'}")
        
        while True:
            print(f"{''.join(stack):<20} | {''.join(buffer):<20} | ", end="")
            
            # Check for reduction
            reduced = False
            for lhs, rhs in self.rules:
                if ''.join(stack).endswith(rhs):
                    stack = stack[:-len(rhs)] + [lhs]
                    print(f"REDUCE {lhs} -> {rhs}")
                    reduced = True
                    break
                    
            if not reduced:
                if buffer[0] == '$':
                    if stack == [self.rules[0][0]]:
                        print("ACCEPT")
                        return True
                    else:
                        print("REJECT")
                        return False
                # Shift
                stack.append(buffer.pop(0))
                print("SHIFT")

if __name__ == '__main__':
    sr = ShiftReduceParser([('E', 'E+E'), ('E', 'E*E'), ('E', 'id')])
    sr.parse(['id', '+', 'id', '*', 'id'])
