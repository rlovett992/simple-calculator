def menu():
    print("Addition: 1")
    print("Subtraction: 2")
    print("Mutiplication: 3")
    print("Division: 4")
    print("Exit: 0")
    return

print("Simple Calculator")

while True:
    menu()
    selection = input("Make your selection: ")
    
    if selection == "0":
        break
    elif selection == "1":
        num1 = float(input("What is the first number: "))
        num2 = float(input("What is the second number: "))
        total = num1 + num2
        print(total)
    elif selection == "2":
        num1 = float(input("What is the first number: "))
        num2 = float(input("What is the second number: "))
        total = num1 - num2
        print(total)
    elif selection == "3":
        num1 = float(input("What is the first number: "))
        num2 = float(input("What is the second number: "))
        total = num1 * num2
        print(total)
    elif selection == "4":
        num1 = float(input("What is the first number: "))
        num2 = float(input("What is the second number: "))
        if num2 == 0:
            print("Error: division by zero")
        else:
            total = num1 / num2
            print(total)