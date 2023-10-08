equation = input()
equation_parts = []
current_number = ''
for char in equation:
    if char.isdigit() or char == '.':
        current_number += char
    else:
        if current_number:
            equation_parts.append(current_number)
            current_number = ''
        equation_parts.append(char)

if current_number:
    equation_parts.append(current_number)
reversed_equation = ''.join(equation_parts[::-1])
print(reversed_equation)
