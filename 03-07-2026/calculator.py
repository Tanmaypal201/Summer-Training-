def calculator():
    num1 = float(input("Enter First Number: "))
    op = input("Enter Operator (+, -, *, /): ")
    num2 = float(input("Enter Second Number: "))

    match op:
        case "+":
            print("Result =", num1 + num2)

        case "-":
            print("Result =", num1 - num2)

        case "*":
            print("Result =", num1 * num2)

        case "/":
            if num2 != 0:
                print("Result =", num1 / num2)
            else:
                print("Error! Division by zero is not allowed.")

        case _:
            print("Invalid Operator!")


while True:
    calculator()

    choice = input("\nDo you want to continue? (Y/N): ").lower()

    if choice != "y":
        print("\nThank You for using the Calculator!")
        break