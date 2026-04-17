from dataclasses import dataclass, field
from typing import List, Optional, Set

@dataclass
class State:
    id: int
    is_end: bool = False
    transitions: dict = field(default_factory=dict)
    epsilon_transitions: List['State'] = field(default_factory=list)

class NFA:
    def __init__(self, start: State, end: State):
        self.start = start
        self.end = end

class ThompsonNFA:
    def __init__(self):
        self.state_counter = 0

    def new_state(self) -> State:
        self.state_counter += 1
        return State(id=self.state_counter)

    def create_basic_nfa(self, symbol: str) -> NFA:
        start, end = self.new_state(), self.new_state()
        start.transitions[symbol] = [end]
        return NFA(start, end)

    def concat(self, nfa1: NFA, nfa2: NFA) -> NFA:
        nfa1.end.epsilon_transitions.append(nfa2.start)
        return NFA(nfa1.start, nfa2.end)

    def union(self, nfa1: NFA, nfa2: NFA) -> NFA:
        start, end = self.new_state(), self.new_state()
        start.epsilon_transitions.extend([nfa1.start, nfa2.start])
        nfa1.end.epsilon_transitions.append(end)
        nfa2.end.epsilon_transitions.append(end)
        return NFA(start, end)

    def kleene_star(self, nfa: NFA) -> NFA:
        start, end = self.new_state(), self.new_state()
        start.epsilon_transitions.extend([nfa.start, end])
        nfa.end.epsilon_transitions.extend([nfa.start, end])
        return NFA(start, end)

if __name__ == '__main__':
    builder = ThompsonNFA()
    nfa_a = builder.create_basic_nfa('a')
    nfa_b = builder.create_basic_nfa('b')
    nfa_ab = builder.concat(nfa_a, nfa_b)
    print(f"NFA start state: {nfa_ab.start.id}, end state: {nfa_ab.end.id}")
