def compute_first(grammar, non_terminals, terminals):
    first = {nt: set() for nt in non_terminals}

    def first_of(symbol):
        if symbol in terminals:
            return {symbol}
        if symbol == 'ε':
            return {'ε'}
        return first[symbol]

    changed = True
    while changed:
        changed = False
        for nt in non_terminals:
            for prod in grammar[nt]:
                i = 0
                while i < len(prod):
                    sym = prod[i]
                    sym_first = first_of(sym)

                    before = len(first[nt])
                    first[nt].update(sym_first - {'ε'})

                    if 'ε' not in sym_first:
                        break
                    i += 1
                else:
                    first[nt].add('ε')

                if len(first[nt]) != before:
                    changed = True

    return first


def compute_follow(grammar, non_terminals, terminals, first, start_symbol):
    follow = {nt: set() for nt in non_terminals}
    follow[start_symbol].add('$')

    changed = True
    while changed:
        changed = False
        for nt in non_terminals:
            for prod in grammar[nt]:
                for i in range(len(prod)):
                    symbol = prod[i]
                    if symbol in non_terminals:
                        trailer = set()
                        if i + 1 < len(prod):
                            next_sym = prod[i + 1]
                            trailer = first[next_sym] - {'ε'}
                            before = len(follow[symbol])
                            follow[symbol].update(trailer)

                            if 'ε' in first[next_sym]:
                                follow[symbol].update(follow[nt])
                        else:
                            before = len(follow[symbol])
                            follow[symbol].update(follow[nt])

                        if len(follow[symbol]) != before:
                            changed = True

    return follow


# ---------------- MAIN PROGRAM ----------------

grammar = {}
non_terminals = set()
terminals = set()

n = int(input("Enter number of productions: "))

for _ in range(n):
    rule = input("Enter production (example E->TE'): ").strip()
    left, right = rule.split("->")
    left = left.strip()
    non_terminals.add(left)

    productions = right.split("|")
    grammar[left] = []

    for prod in productions:
        symbols = []
        i = 0
        while i < len(prod):
            if prod[i].isupper():
                symbols.append(prod[i])
                i += 1
            elif prod[i:i+2] == "id":
                symbols.append("id")
                terminals.add("id")
                i += 2
            else:
                symbols.append(prod[i])
                terminals.add(prod[i])
                i += 1
        grammar[left].append(symbols)

start_symbol = list(grammar.keys())[0]

first = compute_first(grammar, non_terminals, terminals)
follow = compute_follow(grammar, non_terminals, terminals, first, start_symbol)

print("\nFIRST Sets:")
for nt in non_terminals:
    print(f"FIRST({nt}) = {first[nt]}")

print("\nFOLLOW Sets:")
for nt in non_terminals:
    print(f"FOLLOW({nt}) = {follow[nt]}")