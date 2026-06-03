import math
from menus import *
from menu_hadler import *

print("Calculator Project")

while True:
    main_menu()
    selection = input("Make your selection: ")
    
    if selection == "0":
        break
    elif selection == "1":
        num1 = float(input("What is the first number: "))
        num2 = float(input("What is the second number: "))
        total = num1 + num2
        print("The total of", num1, "+", num2, "is", total)
    elif selection == "2":
        num1 = float(input("What is the first number: "))
        num2 = float(input("What is the second number: "))
        total = num1 - num2
        print("The total of", num1, "-", num2, "is", total)
    elif selection == "3":
        num1 = float(input("What is the first number: "))
        num2 = float(input("What is the second number: "))
        total = num1 * num2
        print("The total of", num1, "*", num2, "is", total)
    elif selection == "4":
        num1 = float(input("What is the first number: "))
        num2 = float(input("What is the second number: "))
        if num2 == 0:
            print("Error: division by zero")
        else:
            total = num1 / num2
            print("The total of", num1, "/", num2, "is", total)
    elif selection == "5":
        num1 = float(input("What is the first number: "))
        num2 = float(input("What is the second number: "))
        total = num1 ** num2
        print("The total of", num1, "raised to the", num2, "power is", total)
    elif selection == "6":
        num1 = float(input("What is the first number: "))
        num2 = float(input("What is the second number: "))
        if num2 == 0:
            print("Error: division by zero")
        else:
            total = num1 % num2
            print("The remainder of", num1, "/", num2, "is", total)
    elif selection == "7":
        num1 = float(input("What is the first number: "))
        num2 = float(input("What is the second number: "))
        if num2 == 0:
            print("Error: division by zero")
        else:
            total = num1 // num2
            print(num1, "floor divided by", num2, "is", total)
    elif selection == "8":
        num1 = float(input("What is the number: "))
        if num1 < 0:
            num = abs(num1)
            total = math.sqrt(num)
            print("The square root of", num1, "is", str(total) + "i")
        else:
            total = math.sqrt(num1)
            print("The square root of", num1, "is", total)
    elif selection == "9":
        num1 = float(input("What is the number: "))
        total = abs(num1)
        print("The absolute value of", num1, "is", total)
    elif selection == "10":
        handle_functions_menu()
    else:
        print("You must pick a valid option from the list")