from menus import *

def not_added():
    print("This function has not been added yet.")


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
        elif selection in ["1", "2", "3", "4", "5"]:
            not_added()
        else:
            print("You must pick a valid option from the list")


def handle_geometry_menu():
    while True:
        geometry_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break
        elif selection in ["1", "2", "3"]:
            not_added()
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
        elif selection in ["1", "2", "3", "4"]:
            not_added()
        else:
            print("You must pick a valid option from the list")


def handle_circumference_menu():
    while True:
        circumference_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break
        elif selection in ["1", "2", "3", "4"]:
            not_added()
        else:
            print("You must pick a valid option from the list")


def handle_shape_volume_menu():
    while True:
        shape_volume_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break
        elif selection in ["1", "2"]:
            not_added()
        else:
            print("You must pick a valid option from the list")


def handle_trigonometry_menu():
    while True:
        trigonometry_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break
        elif selection in ["1", "2", "3", "4", "5", "6", "7"]:
            not_added()
        else:
            print("You must pick a valid option from the list")


def handle_financial_menu():
    while True:
        financial_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break
        elif selection in ["1", "2", "3", "4", "5"]:
            not_added()
        else:
            print("You must pick a valid option from the list")


def handle_physics_engineering_menu():
    while True:
        physics_engineering_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break
        elif selection in ["1", "2", "3"]:
            not_added()
        else:
            print("You must pick a valid option from the list")


def handle_number_theory_menu():
    while True:
        number_theory_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break
        elif selection in ["1", "2", "3", "4"]:
            not_added()
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
            not_added()
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
        elif selection in ["1", "2", "3"]:
            not_added()
        else:
            print("You must pick a valid option from the list")


def handle_weight_conversions_menu():
    while True:
        weight_conversions_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break
        elif selection in ["1", "2"]:
            not_added()
        else:
            print("You must pick a valid option from the list")


def handle_volume_conversions_menu():
    while True:
        volume_conversions_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break
        elif selection in ["1", "2"]:
            not_added()
        else:
            print("You must pick a valid option from the list")


def handle_time_conversions_menu():
    while True:
        time_conversions_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break
        elif selection in ["1", "2", "3"]:
            not_added()
        else:
            print("You must pick a valid option from the list")


def handle_health_menu():
    while True:
        health_menu()
        selection = input("Make your selection: ")

        if selection == "0":
            break
        elif selection == "1":
            not_added()
        else:
            print("You must pick a valid option from the list")