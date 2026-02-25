
def compute_first(grammar, non_terminals, terminals):
    first = {nt: set() for nt in non_terminals}

    changed = True
    while changed:
        changed = False
        for nt in non_terminals:
            for prod in grammar[nt]:
                for symbol in prod:
                    if symbol in terminals:
                        before = len(first[nt])
                        first[nt].add(symbol)
                        if len(first[nt]) != before:
                            changed = True
                        break
                    elif symbol in non_terminals:
                        before = len(first[nt])
                        first[nt].update(first[symbol] - {'ε'})
                        if 'ε' not in first[symbol]:
                            break
                        if len(first[nt]) != before:
                            changed = True
                    elif symbol == 'ε':
                        first[nt].add('ε')
                        break
                else:
                    first[nt].add('ε')
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
                        next_symbols = prod[i + 1:]

                        if next_symbols:
                            temp_first = set()
                            for sym in next_symbols:
                                if sym in terminals:
                                    temp_first.add(sym)
                                    break
                                else:
                                    temp_first.update(first[sym] - {'ε'})
                                    if 'ε' not in first[sym]:
                                        break
                            else:
                                temp_first.add('ε')

                            before = len(follow[symbol])
                            follow[symbol].update(temp_first - {'ε'})

                            if 'ε' in temp_first:
                                follow[symbol].update(follow[nt])

                            if len(follow[symbol]) != before:
                                changed = True
                        else:
                            before = len(follow[symbol])
                            follow[symbol].update(follow[nt])
                            if len(follow[symbol]) != before:
                                changed = True
    return follow



def construct_parsing_table(grammar, non_terminals, terminals, first, follow):
    table = {nt: {t: "" for t in terminals.union({'$'})} for nt in non_terminals}

    for nt in non_terminals:
        for prod in grammar[nt]:
            first_set = set()

            if prod[0] in terminals:
                first_set.add(prod[0])
            else:
                first_set.update(first[prod[0]])

            for terminal in first_set - {'ε'}:
                table[nt][terminal] = nt + "->" + "".join(prod)

            if 'ε' in first_set:
                for terminal in follow[nt]:
                    table[nt][terminal] = nt + "->ε"

    return table



grammar = {}
non_terminals = set()
terminals = set()

n = int(input("Enter number of productions: "))

for _ in range(n):
    rule = input("Enter production (Example E->TE'): ").strip()
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
            elif prod[i] == 'ε':
                symbols.append('ε')
                i += 1
            else:
                symbols.append(prod[i])
                terminals.add(prod[i])
                i += 1
        grammar[left].append(symbols)

start_symbol = list(grammar.keys())[0]

first = compute_first(grammar, non_terminals, terminals)
follow = compute_follow(grammar, non_terminals, terminals, first, start_symbol)
parsing_table = construct_parsing_table(grammar, non_terminals, terminals, first, follow)


print("\nFIRST Sets:")
for nt in non_terminals:
    print(f"FIRST({nt}) = {first[nt]}")

print("\nFOLLOW Sets:")
for nt in non_terminals:
    print(f"FOLLOW({nt}) = {follow[nt]}")

print("\nPredictive Parsing Table:\n")

header = list(terminals) + ['$']
print(f"{'NT/T':<10}", end="")
for t in header:
    print(f"{t:<15}", end="")
print()

for nt in non_terminals:
    print(f"{nt:<10}", end="")
    for t in header:
        print(f"{parsing_table[nt][t]:<15}", end="")
    print()