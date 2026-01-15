def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a*b

def devide(a,b):
    if b == 0:
        raise ValueError("The denominator cannot be 0")
    else:
        return a/b

def main():
    a = 2
    b = 2
    print(add(a,b))
    print(subtract(a,b))
    print(multiply(a,b))
    print(devide(a,b))

if __name__ == "__main__":
    main()