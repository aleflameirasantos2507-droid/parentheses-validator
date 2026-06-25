# Parentheses Validator

A beginner-friendly Python project that checks whether the parentheses in a mathematical or logical expression are correctly balanced.

The program uses a stack-based algorithm, a common technique in computer science for validating expressions.

## Features

- Reads an expression from the user
- Detects opening and closing parentheses
- Validates balanced parentheses
- Uses a stack implemented with a Python list
- Reports whether the expression is valid

## Technologies Used

- Python 3

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/parentheses-validator.git
```

2. Navigate to the project folder:

```bash
cd parentheses-validator
```

3. Run the script:

```bash
python main.py
```

## Example

### Valid Expression

```text
Enter an expression: (a + b) * (c - d)
```

Output:

```text
The expression is valid!
```

### Invalid Expression

```text
Enter an expression: ((a + b)
```

Output:

```text
The expression is not valid!
```

## Learning Objectives

This project demonstrates:

- Lists as stacks
- Stack operations (`append` and `pop`)
- Loops (`for`)
- Conditional statements
- Expression validation
- Algorithmic thinking

## How the Algorithm Works

### Opening Parenthesis

When the program finds:

```text
(
```

it pushes it onto the stack:

```python
stack.append('(')
```

### Closing Parenthesis

When the program finds:

```text
)
```

it removes one opening parenthesis from the stack:

```python
stack.pop()
```

### Validation

At the end:

- Empty stack → Valid expression
- Non-empty stack → Invalid expression
