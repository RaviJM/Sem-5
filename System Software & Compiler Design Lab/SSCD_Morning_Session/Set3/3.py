def remove_left_recursion(grammar):
    new_grammar = {}

    for non_terminal in grammar:
        productions = grammar[non_terminal]

        # Split productions into those with and without left recursion
        recursive_productions = [prod for prod in productions if prod.startswith(non_terminal)]
        non_recursive_productions = [prod for prod in productions if not prod.startswith(non_terminal)]

        if recursive_productions:
            # Create a new non-terminal for the non-recursive part
            new_non_terminal = non_terminal + "'"
            new_grammar[non_terminal] = [prod + new_non_terminal for prod in non_recursive_productions]
            new_grammar[new_non_terminal] = [prod[len(non_terminal):] + new_non_terminal for prod in recursive_productions] + ["ε"]
        else:
            new_grammar[non_terminal] = productions

    return new_grammar

def display_grammar(grammar):
    for non_terminal, productions in grammar.items():
        print(f"{non_terminal} -> {' | '.join(productions)}")

if __name__ == "__main__":
    # Define your grammar here
    input_grammar = {
        "S": ["SAB", "B"],
        "A": ["AS", "b"],
        "B": ["c"]
    }

    print("Original Grammar:")
    display_grammar(input_grammar)

    transformed_grammar = remove_left_recursion(input_grammar)

    print("\nGrammar after Left Recursion Removal:")
    display_grammar(transformed_grammar)
