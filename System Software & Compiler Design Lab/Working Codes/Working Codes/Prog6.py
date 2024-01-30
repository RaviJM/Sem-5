from collections import defaultdict

# Example grammar
grammar = {
    'E': ['E + T', 'T'],
    'T': ['T * F', 'F'],
    'F': ['( E )', 'id']
}

# Extract the set of terminals and non-terminals
terminals = set()
non_terminals = set()

for lhs, rhs in grammar.items():
    non_terminals.add(lhs)
    for symbols in rhs:
        for symbol in symbols.split():
            if symbol not in non_terminals:
                terminals.add(symbol)

terminals.add('$')

# Initialize the table with empty cells
table = defaultdict(lambda: defaultdict(str))

for t1 in terminals:
    for t2 in terminals:
        table[t1][t2] = ''

# Fill in the table with precedence relations
for lhs, rhs in grammar.items():
    for i in range(len(rhs)):
        symbols = rhs[i].split()
        for j in range(len(symbols) - 1):
            left = symbols[j]
            right = symbols[j + 1]

            if right in non_terminals:
                # Add all symbols that can follow the right symbol
                for follow in terminals:
                    table[right][follow] += '<'
            elif left in non_terminals:
                # Add all symbols that can precede the left symbol
                for precede in terminals:
                    table[precede][left] += '>'
            elif left == '(' and right == ')':
                # Parentheses have the highest precedence
                pass
            else:
                # Compare the precedence of the two adjacent symbols
                table[left][right] += '=' if left == right == '+' or left == right == '*' else '<' if left == '+' or right == '*' else '>'

# Print the table
print(' ' * 4, end='')
for t in terminals:
    print(f'{t:^4}', end='')
print()

for t1 in terminals:
    print(f'{t1:^4}', end='')
    for t2 in terminals:
        print(f'{table[t1][t2]:^4}', end='')
    print()
