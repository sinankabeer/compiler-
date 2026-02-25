def left_factoring():
    grammar = {}

    print("Enter number of non-terminals:")
    n = int(input())

    for _ in range(n):
        nt = input("Enter non-terminal: ").strip()
        productions = input(
            f"Enter productions for {nt} (use | as separator): "
        ).split("|")

        grammar[nt] = [p.strip() for p in productions]

    print("\nGiven Grammar:")
    for nt, prods in grammar.items():
        print(f"{nt} -> {' | '.join(prods)}")

    print("\nGrammar after Left Factoring:\n")

    new_grammar = {}

    for nt, prods in grammar.items():
        prefix_dict = {}

        
        for prod in prods:
            prefix = prod[0]
            prefix_dict.setdefault(prefix, []).append(prod)

        new_grammar[nt] = []

        for prefix, grouped_prods in prefix_dict.items():
            if len(grouped_prods) > 1:
                new_nt = nt + "'"
                new_grammar[nt].append(prefix + new_nt)

                new_grammar[new_nt] = [
                    p[1:] if len(p) > 1 else "ε"
                    for p in grouped_prods
                ]
            else:
                new_grammar[nt].append(grouped_prods[0])

    for nt, prods in new_grammar.items():
        print(f"{nt} -> {' | '.join(prods)}")



left_factoring()