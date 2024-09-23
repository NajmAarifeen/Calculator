def addition(a,b):
    return a + b
def subtraction(a,b):
    return a - b
def multiplication(a,b):
    return a * b
def division(a,b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def calculator(operations, numbers):
    result = numbers[0]
    for operation, num in zip(operations, numbers[1:]):
        if operation == '+':
            result = addition(result, num)
        elif operation == '-':
            result = subtraction(result, num)
        elif operation == '*':
            result = multiplication(result, num)
        elif operation == '/':
            result = division(result, num)
        else:
            raise ValueError(f"Invalid operation: {operation}")
    return result

operations = ['+', '*', '-']
print(operations, "choose an operations:")

while True:
    try:
        choice = input().strip()
        if choice not in operations:
            raise ValueError(f"Invalid operation: {choice}")
        numbers = list(map(float, input("Enter numbers separated by space: ").split()))
        if len(numbers) < 2:
            raise ValueError("At least two numbers are required")
        result = calculator(operations[:operations.index(choice) + 1], numbers)
        print(f"Result: {result}")
        break
    except ValueError as e:
        print(str(e))


