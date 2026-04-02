def createFile(name):
    try:
        with open(name, "x") as file:
            print("\nFile created successfully!\n")
    except FileExistsError:
        print("\nFile already exists!\n")


def appendFile(name):
    try:
        with open(name, "r"):
            pass
    except FileNotFoundError:
        print("\nFile not found! Create file first.\n")
        return

    data = input("Enter your journal entry:\n")

    with open(name, "a") as file:
        file.write(data + "\n")

    print("\nEntry added successfully!\n")


def readFile(name):
    try:
        with open(name, "r") as file:
            content = file.readlines()

            if not content:
                print("\nNo entries found.\n")
            else:
                print("\nJournal Entries")
                for i, line in enumerate(content, 1):
                    print(f"{i}. {line.strip()}")
                print()

    except FileNotFoundError:
        print("\nFile not found!\n")


def searchEntry(name):
    try:
        keyword = input("Enter keyword to search: ")
        found = False

        with open(name, "r") as file:
            for line in file:
                if keyword.lower() in line.lower():
                    print("Found:", line.strip())
                    found = True

        if not found:
            print("\nNo match found.\n")

    except FileNotFoundError:
        print("\nFile not found!\n")


def clearFile(name):
    try:
        confirm = input("Delete all entries? (yes/no): ")
        if confirm.lower() == "yes":
            open(name, "w").close()
            print("\nAll entries deleted!\n")
        else:
            print("\nCancelled!\n")
    except FileNotFoundError:
        print("\nFile not found!\n")


filename = "journal.txt"

while True:
    print(" Welcome To Personal Journal Manager !\n")
    print("Please select an Option")
    print("1. Create File")
    print("2. Add Entry")
    print("3. View Entries")
    print("4. Search Entry")
    print("5. Delete All Entries")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        createFile(filename)

    elif choice == "2":
        appendFile(filename)

    elif choice == "3":
        readFile(filename)

    elif choice == "4":
        searchEntry(filename)

    elif choice == "5":
        clearFile(filename)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("\nInvalid choice!\n")