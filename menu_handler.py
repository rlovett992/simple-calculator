from menus import *
import math


def handle_functions_menu():
    while True:
        functions_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break
        elif selection == "1":
            handle_algebra_menu()
        elif selection == "2":
            handle_geometry_menu()
        elif selection == "3":
            handle_trigonometry_menu()
        elif selection == "4":
            handle_financial_menu()
        elif selection == "5":
            handle_physics_engineering_menu()
        elif selection == "6":
            handle_number_theory_menu()
        elif selection == "7":
            handle_conversions_menu()
        elif selection == "8":
            handle_health_menu()
        else:
            print("You must pick a valid option from the list")


def handle_algebra_menu():
    while True:
        algebra_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break

        elif selection == "1":
            x1 = float(input("What is the first x: "))
            x2 = float(input("What is the second x: "))
            y1 = float(input("What is the first y: "))
            y2 = float(input("What is the second y: "))

            if x2 - x1 == 0:
                print("The slope is undefined")
            else:
                total = (y2 - y1) / (x2 - x1)
                print("The slope of the line is", total)

        elif selection == "2":
            a = float(input("What is the coefficient of x^2: "))
            b = float(input("What is the coefficient of x: "))
            c = float(input("What is the constant term: "))

            if a == 0:
                print("The coefficient of x^2 cannot be 0")
            else:
                discriminant = b**2 - 4*a*c

                if discriminant > 0:
                    root1 = (-b + math.sqrt(discriminant)) / (2*a)
                    root2 = (-b - math.sqrt(discriminant)) / (2*a)
                    print("The roots are", root1, "and", root2)
                elif discriminant == 0:
                    root = -b / (2*a)
                    print("The root is", root)
                else:
                    real_part = -b / (2*a)
                    imaginary_part = math.sqrt(-discriminant) / (2*a)
                    print("The roots are", str(real_part) + " + " + str(imaginary_part) + "i", "and", str(real_part) + " - " + str(imaginary_part) + "i")

        elif selection == "3":
            print("Solving ax + b = c")
            a = float(input("What is a: "))
            b = float(input("What is b: "))
            c = float(input("What is c: "))

            if a == 0:
                print("a cannot be 0")
            else:
                x = (c - b) / a
                print("x =", x)

        elif selection == "4":
            number = float(input("What number are you taking the log of: "))
            base = float(input("What is the base: "))

            if number <= 0 or base <= 0 or base == 1:
                print("The number and base must be positive, and the base cannot be 1")
            else:
                print("The logarithm is", math.log(number, base))

        elif selection == "5":
            number = float(input("What number are you taking the natural log of: "))

            if number <= 0:
                print("The number must be positive")
            else:
                print("The natural log is", math.log(number))

        else:
            print("You must pick a valid option from the list")


def handle_geometry_menu():
    while True:
        geometry_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break

        elif selection == "1":
            x1 = float(input("What is the first x: "))
            y1 = float(input("What is the first y: "))
            x2 = float(input("What is the second x: "))
            y2 = float(input("What is the second y: "))
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            print("The distance is", distance)

        elif selection == "2":
            x1 = float(input("What is the first x: "))
            y1 = float(input("What is the first y: "))
            x2 = float(input("What is the second x: "))
            y2 = float(input("What is the second y: "))
            midpoint_x = (x1 + x2) / 2
            midpoint_y = (y1 + y2) / 2
            print("The midpoint is", "(" + str(midpoint_x) + ", " + str(midpoint_y) + ")")

        elif selection == "3":
            a = float(input("What is side a: "))
            b = float(input("What is side b: "))
            c = math.sqrt(a**2 + b**2)
            print("The hypotenuse is", c)

        elif selection == "4":
            handle_shape_area_menu()
        elif selection == "5":
            handle_circumference_menu()
        elif selection == "6":
            handle_shape_volume_menu()
        else:
            print("You must pick a valid option from the list")


def handle_shape_area_menu():
    while True:
        shape_area_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break
        elif selection == "1":
            base = float(input("What is the base: "))
            height = float(input("What is the height: "))
            print("The triangle area is", 0.5 * base * height)
        elif selection == "2":
            length = float(input("What is the length: "))
            width = float(input("What is the width: "))
            print("The rectangle area is", length * width)
        elif selection == "3":
            side = float(input("What is the side length: "))
            print("The square area is", side**2)
        elif selection == "4":
            radius = float(input("What is the radius: "))
            print("The circle area is", math.pi * radius**2)
        else:
            print("You must pick a valid option from the list")


def handle_circumference_menu():
    while True:
        circumference_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break
        elif selection == "1":
            radius = float(input("What is the radius: "))
            print("The circle circumference is", 2 * math.pi * radius)
        elif selection == "2":
            length = float(input("What is the length: "))
            width = float(input("What is the width: "))
            print("The rectangle perimeter is", 2 * (length + width))
        elif selection == "3":
            side = float(input("What is the side length: "))
            print("The square perimeter is", 4 * side)
        elif selection == "4":
            side1 = float(input("What is side 1: "))
            side2 = float(input("What is side 2: "))
            side3 = float(input("What is side 3: "))
            print("The triangle perimeter is", side1 + side2 + side3)
        else:
            print("You must pick a valid option from the list")


def handle_shape_volume_menu():
    while True:
        shape_volume_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break
        elif selection == "1":
            side = float(input("What is the side length: "))
            print("The cube volume is", side**3)
        elif selection == "2":
            length = float(input("What is the length: "))
            width = float(input("What is the width: "))
            height = float(input("What is the height: "))
            print("The rectangular prism volume is", length * width * height)
        else:
            print("You must pick a valid option from the list")


def handle_trigonometry_menu():
    while True:
        trigonometry_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break

        elif selection in ["1", "2", "3", "4", "5", "6"]:
            degrees = float(input("What is the angle in degrees: "))
            radians = math.radians(degrees)

            if selection == "1":
                print("The sine is", math.sin(radians))
            elif selection == "2":
                print("The cosine is", math.cos(radians))
            elif selection == "3":
                print("The tangent is", math.tan(radians))
            elif selection == "4":
                cos_value = math.cos(radians)
                if cos_value == 0:
                    print("Secant is undefined")
                else:
                    print("The secant is", 1 / cos_value)
            elif selection == "5":
                sin_value = math.sin(radians)
                if sin_value == 0:
                    print("Cosecant is undefined")
                else:
                    print("The cosecant is", 1 / sin_value)
            elif selection == "6":
                tan_value = math.tan(radians)
                if tan_value == 0:
                    print("Cotangent is undefined")
                else:
                    print("The cotangent is", 1 / tan_value)

        elif selection == "7":
            print("Degrees to radians: 1")
            print("Radians to degrees: 2")
            conversion = input("Make your selection: ")

            if conversion == "1":
                degrees = float(input("What is the degree value: "))
                print("The radian value is", math.radians(degrees))
            elif conversion == "2":
                radians = float(input("What is the radian value: "))
                print("The degree value is", math.degrees(radians))
            else:
                print("You must pick a valid option from the list")

        else:
            print("You must pick a valid option from the list")


def handle_financial_menu():
    while True:
        financial_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break

        elif selection == "1":
            principal = float(input("What is the principal amount: "))
            rate = float(input("What is the annual interest rate as a percent: ")) / 100
            times_compounded = float(input("How many times is it compounded per year: "))
            years = float(input("How many years: "))
            total = principal * (1 + rate / times_compounded) ** (times_compounded * years)
            print("The final amount is", total)

        elif selection == "2":
            principal = float(input("What is the principal amount: "))
            rate = float(input("What is the annual interest rate as a percent: ")) / 100
            years = float(input("How many years: "))
            interest = principal * rate * years
            print("The simple interest is", interest)

        elif selection == "3":
            loan = float(input("What is the loan amount: "))
            annual_rate = float(input("What is the annual interest rate as a percent: ")) / 100
            years = float(input("How many years is the loan: "))
            monthly_rate = annual_rate / 12
            months = years * 12

            if monthly_rate == 0:
                payment = loan / months
            else:
                payment = loan * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)

            print("The monthly payment is", payment)

        elif selection == "4":
            number = float(input("What is the number: "))
            percent = float(input("What percent do you want to find: "))
            print(str(percent) + "% of", number, "is", number * percent / 100)

        elif selection == "5":
            bill = float(input("What is the bill amount: "))
            tip_percent = float(input("What tip percent do you want to leave: "))
            tip = bill * tip_percent / 100
            total = bill + tip
            print("The tip is", tip)
            print("The total is", total)

        else:
            print("You must pick a valid option from the list")


def handle_physics_engineering_menu():
    while True:
        physics_engineering_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break

        elif selection == "1":
            mass = float(input("What is the mass: "))
            velocity = float(input("What is the velocity: "))
            kinetic_energy = 0.5 * mass * velocity**2
            print("The kinetic energy is", kinetic_energy)

        elif selection == "2":
            current = float(input("What is the current: "))
            resistance = float(input("What is the resistance: "))
            voltage = current * resistance
            print("The voltage is", voltage)

        elif selection == "3":
            x = float(input("What is the x component: "))
            y = float(input("What is the y component: "))
            magnitude = math.sqrt(x**2 + y**2)
            print("The vector magnitude is", magnitude)

        else:
            print("You must pick a valid option from the list")


def handle_number_theory_menu():
    while True:
        number_theory_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break

        elif selection == "1":
            number = int(input("What number do you want the factorial of: "))

            if number < 0:
                print("Factorial is not defined for negative numbers")
            else:
                print("The factorial is", math.factorial(number))

        elif selection == "2":
            number = int(input("What number do you want to check: "))

            if number <= 1:
                print("The number is not prime")
            else:
                is_prime = True

                for i in range(2, int(math.sqrt(number)) + 1):
                    if number % i == 0:
                        is_prime = False

                if is_prime:
                    print("The number is prime")
                else:
                    print("The number is not prime")

        elif selection == "3":
            num1 = int(input("What is the first number: "))
            num2 = int(input("What is the second number: "))
            print("The GCD is", math.gcd(num1, num2))

        elif selection == "4":
            num1 = int(input("What is the first number: "))
            num2 = int(input("What is the second number: "))

            if num1 == 0 or num2 == 0:
                print("The LCM is 0")
            else:
                lcm = abs(num1 * num2) // math.gcd(num1, num2)
                print("The LCM is", lcm)

        else:
            print("You must pick a valid option from the list")


def handle_conversions_menu():
    while True:
        conversions_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break
        elif selection == "1":
            handle_unit_conversions_menu()
        elif selection == "2":
            handle_temperature_conversions_menu()
        else:
            print("You must pick a valid option from the list")


def handle_unit_conversions_menu():
    while True:
        unit_conversions_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break
        elif selection == "1":
            handle_length_conversions_menu()
        elif selection == "2":
            handle_weight_conversions_menu()
        elif selection == "3":
            handle_volume_conversions_menu()
        elif selection == "4":
            handle_time_conversions_menu()
        else:
            print("You must pick a valid option from the list")


def handle_length_conversions_menu():
    while True:
        length_conversions_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break

        elif selection == "1":
            print("Miles to kilometers: 1")
            print("Kilometers to miles: 2")
            conversion = input("Make your selection: ")
            value = float(input("What is the value: "))

            if conversion == "1":
                print("The converted value is", value * 1.60934)
            elif conversion == "2":
                print("The converted value is", value / 1.60934)
            else:
                print("You must pick a valid option from the list")

        elif selection == "2":
            print("Feet to meters: 1")
            print("Meters to feet: 2")
            conversion = input("Make your selection: ")
            value = float(input("What is the value: "))

            if conversion == "1":
                print("The converted value is", value * 0.3048)
            elif conversion == "2":
                print("The converted value is", value / 0.3048)
            else:
                print("You must pick a valid option from the list")

        elif selection == "3":
            print("Inches to centimeters: 1")
            print("Centimeters to inches: 2")
            conversion = input("Make your selection: ")
            value = float(input("What is the value: "))

            if conversion == "1":
                print("The converted value is", value * 2.54)
            elif conversion == "2":
                print("The converted value is", value / 2.54)
            else:
                print("You must pick a valid option from the list")

        else:
            print("You must pick a valid option from the list")


def handle_weight_conversions_menu():
    while True:
        weight_conversions_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break

        elif selection == "1":
            print("Pounds to kilograms: 1")
            print("Kilograms to pounds: 2")
            conversion = input("Make your selection: ")
            value = float(input("What is the value: "))

            if conversion == "1":
                print("The converted value is", value * 0.453592)
            elif conversion == "2":
                print("The converted value is", value / 0.453592)
            else:
                print("You must pick a valid option from the list")

        elif selection == "2":
            print("Ounces to grams: 1")
            print("Grams to ounces: 2")
            conversion = input("Make your selection: ")
            value = float(input("What is the value: "))

            if conversion == "1":
                print("The converted value is", value * 28.3495)
            elif conversion == "2":
                print("The converted value is", value / 28.3495)
            else:
                print("You must pick a valid option from the list")

        else:
            print("You must pick a valid option from the list")


def handle_volume_conversions_menu():
    while True:
        volume_conversions_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break

        elif selection == "1":
            print("Gallons to liters: 1")
            print("Liters to gallons: 2")
            conversion = input("Make your selection: ")
            value = float(input("What is the value: "))

            if conversion == "1":
                print("The converted value is", value * 3.78541)
            elif conversion == "2":
                print("The converted value is", value / 3.78541)
            else:
                print("You must pick a valid option from the list")

        elif selection == "2":
            print("Cups to milliliters: 1")
            print("Milliliters to cups: 2")
            conversion = input("Make your selection: ")
            value = float(input("What is the value: "))

            if conversion == "1":
                print("The converted value is", value * 236.588)
            elif conversion == "2":
                print("The converted value is", value / 236.588)
            else:
                print("You must pick a valid option from the list")

        else:
            print("You must pick a valid option from the list")


def handle_time_conversions_menu():
    while True:
        time_conversions_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break

        elif selection == "1":
            print("Seconds to minutes: 1")
            print("Minutes to seconds: 2")
            conversion = input("Make your selection: ")
            value = float(input("What is the value: "))

            if conversion == "1":
                print("The converted value is", value / 60)
            elif conversion == "2":
                print("The converted value is", value * 60)
            else:
                print("You must pick a valid option from the list")

        elif selection == "2":
            print("Minutes to hours: 1")
            print("Hours to minutes: 2")
            conversion = input("Make your selection: ")
            value = float(input("What is the value: "))

            if conversion == "1":
                print("The converted value is", value / 60)
            elif conversion == "2":
                print("The converted value is", value * 60)
            else:
                print("You must pick a valid option from the list")

        elif selection == "3":
            print("Hours to days: 1")
            print("Days to hours: 2")
            conversion = input("Make your selection: ")
            value = float(input("What is the value: "))

            if conversion == "1":
                print("The converted value is", value / 24)
            elif conversion == "2":
                print("The converted value is", value * 24)
            else:
                print("You must pick a valid option from the list")

        else:
            print("You must pick a valid option from the list")


def handle_temperature_conversions_menu():
    while True:
        temperature_conversions_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break

        elif selection == "1":
            print("Fahrenheit to Celsius: 1")
            print("Celsius to Fahrenheit: 2")
            conversion = input("Make your selection: ")
            value = float(input("What is the temperature: "))

            if conversion == "1":
                print("The converted temperature is", (value - 32) * 5 / 9)
            elif conversion == "2":
                print("The converted temperature is", value * 9 / 5 + 32)
            else:
                print("You must pick a valid option from the list")

        elif selection == "2":
            print("Celsius to Kelvin: 1")
            print("Kelvin to Celsius: 2")
            conversion = input("Make your selection: ")
            value = float(input("What is the temperature: "))

            if conversion == "1":
                print("The converted temperature is", value + 273.15)
            elif conversion == "2":
                print("The converted temperature is", value - 273.15)
            else:
                print("You must pick a valid option from the list")

        elif selection == "3":
            print("Fahrenheit to Kelvin: 1")
            print("Kelvin to Fahrenheit: 2")
            conversion = input("Make your selection: ")
            value = float(input("What is the temperature: "))

            if conversion == "1":
                print("The converted temperature is", (value - 32) * 5 / 9 + 273.15)
            elif conversion == "2":
                print("The converted temperature is", (value - 273.15) * 9 / 5 + 32)
            else:
                print("You must pick a valid option from the list")

        else:
            print("You must pick a valid option from the list")


def handle_health_menu():
    while True:
        health_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break

        elif selection == "1":
            weight = float(input("What is your weight in pounds: "))
            height = float(input("What is your height in inches: "))

            if height == 0:
                print("Height cannot be 0")
            else:
                bmi = (weight / height**2) * 703
                print("Your BMI is", bmi)

        else:
            print("You must pick a valid option from the list")