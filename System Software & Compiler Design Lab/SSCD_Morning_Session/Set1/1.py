class ThreeAddressCodeGenerator:
    def __init__(self):
        self.temp_count = 0

    def generate_temp(self):
        temp = f'T{self.temp_count}'
        self.temp_count += 1
        return temp

    def generate_code(self, operation, operand1, operand2, result):
        print(f'{result} = {operand1} {operation} {operand2}')

def generate_three_address_code(expression):
    generator = ThreeAddressCodeGenerator()

    # Split the expression into operands and operators
    tokens = expression.replace(' ', '').replace('-', ' - ').replace('+', ' + ').replace('*', ' * ').split()

    result = generator.generate_temp()
    current_operand = tokens[0]

    for token in tokens[1:]:
        if token in {'+', '-', '*'}:
            operation = token
        else:
            temp = generator.generate_temp()
            generator.generate_code(operation, current_operand, token, temp)
            current_operand = temp

    # The final result assignment
    generator.generate_code('=', current_operand, '', result)

if __name__ == "__main__":
    expression = input("Enter the arithmetic expression: ")
    generate_three_address_code(expression)
