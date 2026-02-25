def eliminate_ambiguity_expression_grammar():
    """
    Converts an ambiguous expression grammar into an unambiguous one
    by enforcing operator precedence and associativity.
    """

    unambiguous_grammar = {
        "E": ["T E'"],
        "E'": ["+ T E'", "ε"],
        "T": ["F T'"],
        "T'": ["* F T'", "ε"],
        "F": ["id"]
    }

    return unambiguous_grammar



grammar = eliminate_ambiguity_expression_grammar()

print("Unambiguous Grammar:")
for non_terminal, productions in grammar.items():
    print(f"{non_terminal} -> {' | '.join(productions)}")