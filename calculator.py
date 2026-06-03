import math

""" DEV NOTE """
""""
slope
distance
midpoint
quadratic
pythagorean
sin
cos
tan
secant
cosecant
cotangent
degree <--> radian conversions
shape area
circumfrence
shape volume
mean
median
mode
min
max
standard deviation
compound interest
kinetic energy
ohms law
unit conversions
Percentage calculator
Factorial
Prime number checker
Greatest common divisor
Least common multiple
Random number generator
Temperature conversions
Currency-style tip calculator
BMI calculator
Simple interest
Loan payment calculator
Vector magnitude
Linear equation solver
System of equations solver
Logarithms
Natural log
Graphing functions later with matplotlib
"""

def menu():
    print()
    print("Addition: 1")
    print("Subtraction: 2")
    print("Multiplication: 3")
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
    else:
        print("You must pick a valid option from the list")