import re

def create_symbol_table(program):
    symbol_table = {}

    lines = program.split('\n')
    for line_number, line in enumerate(lines, start=1):
        tokens = re.findall(r'\b\w+\b', line)

        for token in tokens:
            if token not in symbol_table:
                symbol_table[token] = {"Occurrences": [(line_number, line.find(token) + 1)]}
            else:
                symbol_table[token]["Occurrences"].append((line_number, line.find(token) + 1))

    return symbol_table

def display_symbol_table(symbol_table):
    print("Symbol Table:")
    print("{:<15} {:<15}".format("Symbol", "Occurrences"))
    for symbol, attributes in symbol_table.items():
        occurrences = ", ".join([f"({line}, {position})" for line, position in attributes["Occurrences"]])
        print("{:<15} {:<15}".format(symbol, occurrences))

if __name__ == "__main__":
    # Example program
    input_program = """
    int main() {
        int a = 10;
        int b = a * 2;
        return b;
    }
    """

    # Create and display the symbol table
    symbol_table = create_symbol_table(input_program)
    display_symbol_table(symbol_table)
