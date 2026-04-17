from collections import defaultdict
from typing import List, Dict

class GrammarTransformer:
    def __init__(self, grammar: Dict[str, List[str]]):
        self.grammar = defaultdict(list, grammar)

    def eliminate_left_recursion(self):
        new_grammar = defaultdict(list)
        for non_term, productions in self.grammar.items():
            alphas = [p[1:] for p in productions if p.startswith(non_term)]
            betas = [p for p in productions if not p.startswith(non_term)]
            
            if not alphas:
                new_grammar[non_term] = productions
                continue
                
            prime = non_term + "'"
            for beta in betas:
                new_grammar[non_term].append(f"{beta}{prime}")
            for alpha in alphas:
                new_grammar[prime].append(f"{alpha}{prime}")
            new_grammar[prime].append('ε')
            
        self.grammar = new_grammar

    def left_factor(self):
        # A simplified advanced implementation for immediate factoring
        new_grammar = defaultdict(list)
        for non_term, productions in self.grammar.items():
            prefix_map = defaultdict(list)
            for p in productions:
                prefix_map[p[0] if p != 'ε' else 'ε'].append(p)
                
            for prefix, prods in prefix_map.items():
                if len(prods) > 1:
                    prime = non_term + "''"
                    new_grammar[non_term].append(f"{prefix}{prime}")
                    for p in prods:
                        remainder = p[1:] if len(p) > 1 else 'ε'
                        new_grammar[prime].append(remainder)
                else:
                    new_grammar[non_term].extend(prods)
        self.grammar = new_grammar

if __name__ == '__main__':
    g = GrammarTransformer({'E': ['E+T', 'T']})
    g.eliminate_left_recursion()
    print(dict(g.grammar))
