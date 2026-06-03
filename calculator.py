import math

def menu():
    print()
    print("Addition: 1")
    print("Subtraction: 2")
    print("Mutiplication: 3")
    print("Division: 4")
    print("Exponent: 5")
    print("Modulus: 6")
    print("Floor Division: 7")
    print("Square Root: 8")
    print("Absolute Value: 9")
    print("Exit: 0")
    print()
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
    elif selection == "5":
        num1 = float(input("What is the first number: "))
        num2 = float(input("What is the second number: "))
        total = num1 ** num2
        print(total)
    elif selection == "6":
        num1 = float(input("What is the first number: "))
        num2 = float(input("What is the second number: "))
        total = num1 % num2
        print(total)
    elif selection == "7":
        num1 = float(input("What is the first number: "))
        num2 = float(input("What is the second number: "))
        if num2 == 0:
            print("Error: division by zero")
        else:
            total = num1 // num2
            print(total)
    elif selection == "8":
        num1 = float(input("What is the number: "))
        total = math.sqrt(num1)
        print(total)
    elif selection == "9":
        num1 = float(input("What is the number: "))
        total = abs(num1)
        print(total)
    else:
        print("You must pick a valid option from the list")