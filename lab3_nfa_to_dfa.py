from typing import Set, Dict, FrozenSet
from lab2_re_to_nfa import State, NFA, ThompsonNFA

class SubsetConstruction:
    @staticmethod
    def epsilon_closure(states: Set[State]) -> FrozenSet[State]:
        stack = list(states)
        closure = set(states)
        while stack:
            state = stack.pop()
            for next_state in state.epsilon_transitions:
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
        return frozenset(closure)

    @staticmethod
    def move(states: FrozenSet[State], symbol: str) -> Set[State]:
        result = set()
        for state in states:
            if symbol in state.transitions:
                result.update(state.transitions[symbol])
        return result

    @classmethod
    def convert(cls, nfa: NFA, alphabet: Set[str]) -> Dict[FrozenSet[State], Dict[str, FrozenSet[State]]]:
        start_closure = cls.epsilon_closure({nfa.start})
        dfa_states = [start_closure]
        dfa_transitions = {}
        unmarked = [start_closure]

        while unmarked:
            current = unmarked.pop(0)
            dfa_transitions[current] = {}
            for symbol in alphabet:
                next_states = cls.epsilon_closure(cls.move(current, symbol))
                if not next_states: continue
                
                dfa_transitions[current][symbol] = next_states
                if next_states not in dfa_states:
                    dfa_states.append(next_states)
                    unmarked.append(next_states)
                    
        return dfa_transitions

if __name__ == '__main__':
    pass 
