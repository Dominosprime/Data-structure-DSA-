

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None 

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)


def is_balanced(expression):
    s = Stack()
    opening = "([{"
    closing = ")]}"
    match = { ")": "(", "]": "[", "}": "{" } 

    for char in expression:
        if char in opening:
            s.push(char)
        elif char in closing:
            if s.is_empty() or s.pop() != match[char]:
                return False
    return s.is_empty()  


def evaluate_postfix(expression):
    s = Stack()
    operators = "+-*/"

    for token in expression.split():  # Split by spaces
        if token not in operators: #if token is an operand
            try:
                s.push(float(token)) #convert token to float and push onto stack
            except ValueError:
                return "Invalid expression: Operands must be numeric"
        else: #if token is an operator
            operand2 = s.pop()
            operand1 = s.pop()
            if operand1 is None or operand2 is None: #check if operands are available
              return "Invalid expression: Insufficient operands"
            try:
                if token == "+":
                    result = operand1 + operand2
                elif token == "-":
                    result = operand1 - operand2
                elif token == "*":
                    result = operand1 * operand2
                elif token == "/":
                    if operand2 == 0:
                        return "Division by zero"
                    result = operand1 / operand2
                s.push(result)
            except TypeError: #if operand1 or operand2 are not numbers
              return "Invalid expression: Operands must be numeric"
            except Exception as e:
                return f"An error occurred: {e}"
    if s.size() != 1: #check if only the result is left on the stack
      return "Invalid expression"
    return s.pop()


# Example usage:
expression1 = "(2 + [3 * {4 / (5 - 1)}])"
expression2 = "2 3 + 4 * 5 1 - /" #postfix of expression1

if is_balanced(expression1):
    print(f"'{expression1}' is balanced.")
else:
    print(f"'{expression1}' is not balanced.")

result = evaluate_postfix(expression2)
print(f"Result of '{expression2}': {result}")

expression3 = "(2 + [3 * {4 / (5 - 1)}]" #unbalanced expression
if is_balanced(expression3):
    print(f"'{expression3}' is balanced.")
else:
    print(f"'{expression3}' is not balanced.")

expression4 = "2 3 + 4 * 5 1 - / +" #correct postfix expression
result2 = evaluate_postfix(expression4)
print(f"Result of '{expression4}': {result2}")

expression5 = "2 a + 4 * 5 1 - /" #wong postfix expression #operand is not a number
result3 = evaluate_postfix(expression5)
print(f"Result of '{expression5}': {result3}")

expression6 = "2 3 + 4 * 5 1 - / 0 /" #wrong postfix expression # division by zero
result4 = evaluate_postfix(expression6)
print(f"Result of '{expression6}': {result4}")

expression7 = "2 3 + 4 * 5 1 - / +" #wrong postfix expression since operands are not enough
result5 = evaluate_postfix(expression7)
print(f"Result of '{expression7}': {result5}")

expression8 = "2 3 + 4 * 5 1 - /" # correct postfix expression
result6 = evaluate_postfix(expression8)
print(f"Result of '{expression8}': {result6}")