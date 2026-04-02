import os

class JournalManager:
    def _init_(self, filename="journal.txt"):
        self.filename = filename

    
    def create_file(self):
        try:
            if os.path.exists(self.filename):
                print("File already exists.\n")
            else:
                with open(self.filename, "w") as file:  
                    pass
                print("File created successfully!\n")
        except Exception as e:
            print("Error creating file:", e)

   
    def add_entry(self):
        try:
            if not os.path.exists(self.filename):
                print("File does not exist. Please create file first.\n")
                return

            entry = input("Enter your journal entry:\n")
            with open(self.filename, "a") as file:  
                file.write(entry + "\n")

            print("Entry added successfully!\n")
        except Exception as e:
            print("Error adding entry:", e)

   
    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                data = file.readlines()
                if not data:
                    print("No entries found.\n")
                else:
                    print("\n--- Journal Entries ---")
                    for i, line in enumerate(data, 1):
                        print(f"{i}. {line.strip()}")
                    print()
        except FileNotFoundError:
            print("File does not exist.\n")

    
    def search_entry(self):
        try:
            keyword = input("Enter keyword to search: ")
            with open(self.filename, "r") as file:
                found = False
                for line in file:
                    if keyword.lower() in line.lower():
                        print("Found:", line.strip())
                        found = True
                if not found:
                    print("No match found.\n")
        except FileNotFoundError:
            print("File does not exist.\n")

  
    def delete_entries(self):
        try:
            confirm = input("Delete all entries? (yes/no): ")
            if confirm.lower() == "yes":
                open(self.filename, "w").close()
                print("All entries deleted.\n")
            else:
                print("Cancelled.\n")
        except Exception as e:
            print("Error:", e)


def main():
    jm = JournalManager()

    while True:
        print("=== Personal Journal Manager ===")
        print("1. Create File")
        print("2. Add Entry")
        print("3. View All Entries")
        print("4. Search Entry")
        print("5. Delete All Entries")
        print("6. Exit")

        choice = input("Choose (1-6): ")

        if choice == "1":
            jm.create_file()
        elif choice == "2":
            jm.add_entry()
        elif choice == "3":
            jm.view_entries()
        elif choice == "4":
            jm.search_entry()
        elif choice == "5":
            jm.delete_entries()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!\n")


if __name__ == "_main_":
    main()