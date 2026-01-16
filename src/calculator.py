from operator import add, subtract, multiply, divide

def calculate(a, b, operator):
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    if operator not in operations:
        raise ValueError("Invalid operator")

    return operations[operator](a, b)

def main():
    print(calculate(2, 3, "+"))

if __name__ == "__main__":
    main()
