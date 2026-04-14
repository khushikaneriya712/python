import datetime
import random
import uuid
import math


def datetime_menu():
    while True:
        print("\n==============================")
        print("Datetime and Time Operations")
        print("==============================")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
        
            current = datetime.datetime.now()
            print("\nCurrent Date and Time:", current)

        elif choice == "2":
           
            d1 = input("Enter first date (YYYY-MM-DD): ")
            d2 = input("Enter second date (YYYY-MM-DD): ")

            date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
            date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")

            difference = abs((date2 - date1).days)
            print("Difference:", difference, "days")

        elif choice == "3":
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice! Try again.")


def math_menu():
    while True:
        print("\n==============================")
        print("Mathematical Operations")
        print("==============================")
        print("1. Calculate Factorial")
        print("2. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            num = int(input("Enter a number: "))
            result = math.factorial(num)
            print("Factorial of", num, "is:", result)

        elif choice == "2":
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice! Try again.")


def random_menu():
    while True:
        print("\n==============================")
        print("Random Data Generation")
        print("==============================")
        print("1. Generate Random Number")
        print("2. Generate Random Password")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            number = random.randint(1, 100)
            print("Random Number:", number)

        elif choice == "2":
            length = int(input("Enter password length: "))
            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

            password = ""
            for i in range(length):
                password += random.choice(characters)

            print("Generated Password:", password)

        elif choice == "3":
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice! Try again.")


def generate_uuid():
    print("\n==============================")
    print("Generate Unique Identifier")
    print("==============================")

    unique_id = uuid.uuid4()
    print("Generated UUID:", unique_id)


def file_menu():
    while True:
        print("\n==============================")
        print("File Operations")
        print("==============================")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("Enter file name: ")
            file = open(filename, "w")
            file.close()
            print("File created successfully!")

        elif choice == "2":
            filename = input("Enter file name: ")
            data = input("Enter data to write: ")

            with open(filename, "w") as file:
                file.write(data)

            print("Data written successfully!")

        elif choice == "3":
            filename = input("Enter file name: ")

            with open(filename, "r") as file:
                content = file.read()

            print("File Content:")
            print(content)

        elif choice == "4":
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice! Try again.")


def explore_module():
    print("\n==============================")
    print("Explore Module Attributes")
    print("==============================")

    module_name = input("Enter module name (example: math): ")

    module = __import__(module_name)

    print("\nAvailable functions/attributes:")
    print(dir(module))


while True:
    print("\n===================================")
    print("   Welcome to Multi-Utility Toolkit")
    print("===================================")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate UUID")
    print("5. File Operations")
    print("6. Explore Module Attributes (dir)")
    print("7. Exit")

    main_choice = input("Enter your choice: ")

    if main_choice == "1":
        datetime_menu()

    elif main_choice == "2":
        math_menu()

    elif main_choice == "3":
        random_menu()

    elif main_choice == "4":
        generate_uuid()

    elif main_choice == "5":
        file_menu()

    elif main_choice == "6":
        explore_module()

    elif main_choice == "7":
        print("Thank you! Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")