data = []

def input_data():
    global data
    values = input("Enter numbers (space separated): ")
    data = list(map(int, values.split()))
    print("Data stored successfully!\n")


def data_summary():
    if not data:
        print("No data available!\n")
        return

    print("\nData Summary:")
    print("Total elements:", len(data))
    print("Minimum value:", min(data))
    print("Maximum value:", max(data))
    print("Sum:", sum(data))
    print()



def average():
    if not data:
        return 0
    return sum(data) / len(data)


def show_values(*args):
    print("Values using *args:", args)



def show_info(**kwargs):
    print("\nDataset Info:")
    for key, value in kwargs.items():
        print(key, ":", value)


def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)



def filter_data():
    if not data:
        print("No data available!\n")
        return

    t = int(input("Enter threshold: "))
    
    result = []
    for i in data:
        if i > t:
            result.append(i)

    print("Filtered data:", result)
    print()



def sort_data():
    if not data:
        print("No data available!\n")
        return

    print("Ascending:", sorted(data))
    print("Descending:", sorted(data, reverse=True))
    print()

def statistics():
    if not data:
        return (0, 0, 0)

    return (min(data), max(data), average())

while True:
    print("Welcome to Data Analysir and Transforam program")
    print("1. Input Data")
    print("2. Data Summary")
    print("3. Average")
    print("4. Factorial")
    print("5. Filter Data")
    print("6. Sort Data")
    print("7. Show Statistics")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        input_data()

    elif choice == "2":
        data_summary()

    elif choice == "3":
        print("Average:", average(), "\n")

    elif choice == "4":
        num = int(input("Enter number: "))
        print("Factorial:", factorial(num), "\n")

    elif choice == "5":
        filter_data()

    elif choice == "6":
        sort_data()

    elif choice == "7":
        mn, mx, avg = statistics()
        print("Min:", mn)
        print("Max:", mx)
        print("Avg:", avg, "\n")

        show_info(Total=len(data), Sum=sum(data))
        show_values(*data)

    elif choice == "8":
        print("Thank you for using data and transformer program, Good byy!")
        break

    else:
        print("Invalid choice!\n")