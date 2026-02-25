def eliminate_left_recursion():
    grammar = {}

    print("Enter number of non-terminals:")
    n = int(input())

    for _ in range(n):
        non_terminal = input("Enter non-terminal: ").strip()
        productions = input(
            f"Enter productions for {non_terminal} (use | as separator): "
        ).split("|")

        grammar[non_terminal] = [p.strip() for p in productions]

    print("\nGiven Grammar:")
    for nt, prods in grammar.items():
        print(f"{nt} -> {' | '.join(prods)}")

    print("\nGrammar after eliminating left recursion:\n")

    new_grammar = {}

    for nt, prods in grammar.items():
        alpha = []  
        beta = []   

        for prod in prods:
            if prod.startswith(nt):
                alpha.append(prod[len(nt):])
            else:
                beta.append(prod)

        if alpha:
            new_nt = nt + "'"
            new_grammar[nt] = [b + new_nt for b in beta]
            new_grammar[new_nt] = [a + new_nt for a in alpha] + ["ε"]
        else:
            new_grammar[nt] = prods

    for nt, prods in new_grammar.items():
        print(f"{nt} -> {' | '.join(prods)}")



eliminate_left_recursion()