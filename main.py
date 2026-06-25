expression = input('Enter an expression: ')
stack = []

for character in expression:
    if character == '(':
        stack.append('(')

    elif character == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(')')
            break

if len(stack) == 0:
    print('The expression is valid!')
else:
    print('The expression is not valid!')
