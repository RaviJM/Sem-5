def classify_token(token):
    try:
        num = int(token)
        print(f"Number: {num}")
    except ValueError:
        if token in operators:
            print(f"Operator: {token}")
        elif token in delimiters:
            print(f"Delimeter: {token}")
        elif token in keywords:
            print(f"Keyword: {token}")
        else:
            print(f"Identifier: {token}")

operators = {'+', '=', '*', '/', '%', '++', '--', '+=', '-=', '*=', '/=', '%=', '==', '!=', '>', '<', '>=', '<=', '&&', '||', '!', '&', '|', '^', '~', '<<', '>>', '<<=', '>>=', '&=', '|=', '^=', '~='}
delimiters = {';', ',', ':', '.', '(', ')', '{', '}', '[', ']', "'", '"'}
keywords = {'int', 'float', 'char', 'double', 'long', 'short', 'signed', 'unsigned', 'void', 'for', 'while', 'do', 'if', 'else', 'switch', 'case', 'break', 'continue', 'goto', 'default', 'return', 'auto', 'extern', 'register', 'static', 'const', 'sizeof', 'struct', 'typedef', 'union', 'volatile'}

def tokenize_and_classify(line):
    tokens=line.split()
    for token in tokens:
        classify_token(token)

def main():
    try:
        with open("input.txt","r") as file:
            for line in file:
                print(f"The string is entered is {line}")
                tokenize_and_classify(line)
    except FileNotFoundError:
        print("Error opening file.")

if _name=="__main_":
    main()