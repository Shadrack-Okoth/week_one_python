def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

while True:
    print("\nPlease select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    sel = input("Select operation (1-5 only): ")

    if sel == "5":
        print("Exiting the calculator. Goodbye!")
        break

    if sel not in ["1", "2", "3", "4"]:
        print("Invalid selection! Please choose a valid option.")
        continue

    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Only numbers are allowed.")
        continue

    if sel == "1":
        print( x ,"+", y, "=",add(x,y))
    elif sel == "2":
        print( x ,"+", y, "=",sub(x,y))
    elif sel == "3":
        print( x ,"+", y, "=",mul(x,y))
    elif sel == "4":
        if y == 0:
            print("Error! Division by zero is not allowed.")
        else:
            print( x ,"+", y, "=",div(x,y))