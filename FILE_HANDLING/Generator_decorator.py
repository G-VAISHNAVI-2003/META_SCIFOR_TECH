def cal(func):
    def wrapper(op, num1, num2):
        print("CALCULATOR !!")
        res = func(op, num1, num2)
        print("NOT FOUND CALCULATOR!!")
        return res
    return wrapper

@cal
def calculate(op, num1, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by '0'"

def inp():
    while True:
        op = input("Enter operation (+, -, *, /) from the choice: ")
        if op not in ['+', '-', '*', '/']:
            print("Invalid operation....")
            continue
        num1 = float(input("Enter the number 1: "))
        num2 = float(input("Enter the number 2: "))
        yield op, num1, num2

def run():
    user_inp = inp()
    while True:
        op, num1, num2 = next(user_inp)
        res = calculate(op, num1, num2)
        print("The Result is :", res)

run()
