"""
A simple calculator to do basic operators.

Note: currently does not support order of operations
"""
equation   = raw_input("Please enter a mathematical equation: ").split(' ')
numbers    = []
operations = []
for i, x in enumerate(equation):
    if i % 2 == 0:
        numbers.append(x)
    else:
        operations.append(x)

current = int(numbers.pop(0))
while len(numbers) > 0:
    op = operations.pop(0)
    if op == '+':
        current += int(numbers.pop(0))
    elif op == '-':
        current -= int(numbers.pop(0))
    elif op == '/':
        current /= int(numbers.pop(0))
    elif op == '*':
        current *= int(numbers.pop(0))
    else:
        print op, "is an unsupported operator"
        break
print "{} = {}".format(equation,current)
