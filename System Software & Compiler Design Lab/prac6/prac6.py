from tabulate import tabulate
# Take user input for the grammar
no_of_terminals = int(input("Enter no. of terminals: "))
terminals = []
print("Enter the terminals:")
for _ in range(no_of_terminals):
    terminals.append(input())

no_of_non_terminals = int(input("Enter no. of non-terminals: "))
non_terminals = []
print("Enter the non-terminals:")
for _ in range(no_of_non_terminals):
    non_terminals.append(input())

starting_symbol = input("Enter the starting symbol: ")

no_of_productions = int(input("Enter no of productions: "))
productions = []
print("Enter the productions:")
for _ in range(no_of_productions):
    productions.append(input())

# Initialize Firstopp and Lastopp dictionaries
Firstopp = {}
Lastopp = {}

# Helper function to add symbols to Firstopp for a non-terminal

def add_to_Firstopp(non_terminal, symbol):
    if non_terminal not in Firstopp:
        Firstopp[non_terminal] = set()
    Firstopp[non_terminal].add(symbol)

# Helper function to add symbols to Lastopp for a non-terminal

def add_to_Lastopp(non_terminal, symbol):
    if non_terminal not in Lastopp:
        Lastopp[non_terminal] = set()
    Lastopp[non_terminal].add(symbol)

# Initialize the productions_dict
productions_dict = {}

for nT in non_terminals:
    productions_dict[nT] = []

# Print the initialized productions_dict
# print("Initialized productions_dict:")
# for non_terminal, prods in productions_dict.items():
#     print(f"{non_terminal} -> {prods}")

# Parse the user input productions and build the productions_dict
for production in productions:
    nonterm_to_prod = production.split("->")
    alternatives = nonterm_to_prod[1].split("|")
    for alternative in alternatives:
        productions_dict[nonterm_to_prod[0]].append(alternative)

# Print the populated productions_dict
print("Populated productions_dict:")
for non_terminal, prods in productions_dict.items():
    print(f"{non_terminal} -> {prods}")

# Compute Firstopp for each non-terminal
for non_terminal in non_terminals:
    for production in productions_dict[non_terminal]:
        symbols = production.split()
        print(symbols)
        for symbol in symbols:
            if symbol in non_terminals:
                add_to_Firstopp(non_terminal, symbol)
            elif symbol in terminals:
                add_to_Firstopp(non_terminal, symbol)
                break

# Compute Lastopp for each non-terminal
for non_terminal in non_terminals:
    for production in productions_dict[non_terminal]:
        symbols = production.split()
        for symbol in reversed(symbols):
            if symbol in non_terminals:
                add_to_Lastopp(non_terminal, symbol)
            elif symbol in terminals:
                add_to_Lastopp(non_terminal, symbol)
                break

# Print the Firstopp and Lastopp sets
print("Firstopp:")
for non_terminal, first_set in Firstopp.items():
    print(f'Firstopp({non_terminal}) = {{{", ".join(first_set)}}}')

print("Lastopp:")
for non_terminal, last_set in Lastopp.items():
    print(f'Lastopp({non_terminal}) = {{{", ".join(last_set)}}}')

counter = 0
while counter < no_of_productions:
    for non_terminal, first_set in Firstopp.items():
        first_set_copy = first_set.copy()  # Create a copy of the set to iterate over
        for symbol in first_set_copy:
            if symbol in non_terminals:
                Firstopp[non_terminal] |= Firstopp[symbol]
    counter += 1

# Remove non-terminals from Lastopp sets
counter = 0
while counter < no_of_productions:
    for non_terminal, last_set in Lastopp.items():
        last_set_copy = last_set.copy()  # Create a copy of the set to iterate over
        for symbol in last_set_copy:
            if symbol in non_terminals:
                Lastopp[non_terminal] |= Lastopp[symbol]
    counter += 1
# Remove non-terminals from Firstopp sets
for non_terminal, first_set in Firstopp.items():
    first_set_copy = first_set.copy()  # Create a copy of the set to iterate over
    for symbol in first_set_copy:
        if symbol in non_terminals:
            first_set.remove(symbol)

# Remove non-terminals from Lastopp sets
for non_terminal, last_set in Lastopp.items():
    last_set_copy = last_set.copy()  # Create a copy of the set to iterate over
    for symbol in last_set_copy:
        if symbol in non_terminals:
            last_set.remove(symbol)

# Print the modified Firstopp and Lastopp sets
print("Firstop:")
for non_terminal, first_set in Firstopp.items():
    print(f'Firstop({non_terminal}) = {{{", ".join(first_set)}}}')

print("Lastop:")
for non_terminal, last_set in Lastopp.items():
    print(f'Lastop({non_terminal}) = {{{", ".join(last_set)}}}')
# Create an empty matrix with rows and columns for terminals

# Add a dollar symbol ('$') to the terminals list
terminals.append('$')

# Create an empty matrix with rows and columns for terminals
terminal_matrix = [[' ' for _ in range(len(terminals))]
                   for _ in range(len(terminals))]

# Rule 1: Whenever terminal a immediately precedes non-terminal B in any production, put a <·α where α is any terminal in the Firstopp+ list of B
for non_terminal in non_terminals:
    for productions in productions_dict[non_terminal]:
        production = productions.split()
        for i in range(len(production) - 1):
            if production[i] in terminals and production[i + 1] in non_terminals:
                for alpha in Firstopp[production[i + 1]]:
                    row_index = terminals.index(production[i])
                    col_index = terminals.index(alpha)
                    terminal_matrix[row_index][col_index] = '<'

# Rule 2: Whenever terminal b immediately follows non-terminal C in any production, put β ·>b where β is any terminal in the Lastopp+ list of C
for non_terminal in non_terminals:
    for productions in productions_dict[non_terminal]:
        production = productions.split()
        for i in range(1, len(production)):
            if production[i - 1] in non_terminals and production[i] in terminals:
                for beta in Lastopp[production[i - 1]]:
                    row_index = terminals.index(beta)
                    col_index = terminals.index(production[i])
                    terminal_matrix[row_index][col_index] = '>'

# Rule 3: Whenever a sequence aBc or ac occurs in any production, put a ≐ c
for non_terminal in non_terminals:
    for productions in productions_dict[non_terminal]:
        production = productions.split()
        for i in range(1, len(production) - 1):
            if production[i - 1] in terminals and production[i + 1] in terminals:
                row_index = terminals.index(production[i - 1])
                col_index = terminals.index(production[i + 1])
                terminal_matrix[row_index][col_index] = '='

# Rule 4: Add relations $<· a and a ·> $ for all terminals in the Firstopp+ and Lastopp+ lists, respectively of S
for alpha in Firstopp[starting_symbol]:
    col_index = terminals.index(alpha)
    terminal_matrix[-1][col_index] = '<'
for beta in Lastopp[starting_symbol]:
    row_index = terminals.index(beta)
    terminal_matrix[row_index][-1] = '>'

dollar_index = terminals.index('$')
terminal_matrix[-1][dollar_index] = 'acc'
# Map symbols to printable representations

# Add a space for empty cells

# Create a list of lists for the table
table_data = []
for i in range(len(terminals)):
    row = [terminals[i]]
    row.extend([terminal_matrix[i][j] for j in range(len(terminals))])
    table_data.append(row)

# Add headers for columns
headers = [''] + terminals

# Print the table using tabulate
table = tabulate(table_data, headers, tablefmt="grid")

print("Operator Precedence Table:")
print(table)

# Define a function to parse an input expression using the operator precedence table

def parse_expression(expressions):
    stack = ['$']  # Initialize the stack with '$'
    expression = expressions.split()
    # Append '$' to the input expression
    input_buffer = list(expression) + ['$']
    print(input_buffer)
    index = 0  # Index to traverse the input buffer

    while len(stack) > 0:
        top_stack = stack[-1]
        print(top_stack)
        current_input = input_buffer[index]

        # Find the indices of the top of the stack and the current input in the terminal list
        top_stack_index = terminals.index(top_stack)
        current_input_index = terminals.index(current_input)

        # Get the relation from the operator precedence table
        relation = terminal_matrix[top_stack_index][current_input_index]

        if relation == '<' or relation == '=':
            stack.append(current_input)
            index += 1
        elif relation == '>':
            popped = ''
            while relation != '<':
                popped = stack.pop()  # Pop elements from the stack until '<' relation is found
                top_stack = stack[-1] if stack else None
                top_stack_index = terminals.index(
                    top_stack) if top_stack else None
                relation = terminal_matrix[top_stack_index][terminals.index(
                    popped)]
            # stack.append(popped)
        elif relation == 'acc':
            print("Input expression is accepted.")
            return
        else:
            print("Input expression is not accepted.")
            return

# Input an expression to parse
while True:
    choice = int(input(
        "Enter 1 if you want to check if a string is accepted by a parser and 2 if you want to exit"))
    expression_to_parse = input("Enter an expression to parse: ")
    parse_expression(expression_to_parse)
    if choice == 2:
        break
