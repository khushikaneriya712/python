import numpy as np

class DataAnalytics:

    def _init_(self):
        self.arr = None

    def create_array(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            n = int(input("\nEnter number of elements: "))
            data = list(map(int, input("Enter elements separated by space: ").split()))
            self.arr = np.array(data)

        elif ch == 2:
            r = int(input("\nEnter the number of rows: "))
            c = int(input("Enter the number of columns: "))
            data = list(map(int, input(f"Enter {r*c} elements separated by space: ").split()))
            self.arr = np.array(data).reshape(r, c)

        elif ch == 3:
            x = int(input("\nEnter blocks: "))
            y = int(input("Enter rows: "))
            z = int(input("Enter columns: "))
            data = list(map(int, input(f"Enter {x*y*z} elements: ").split()))
            self.arr = np.array(data).reshape(x, y, z)

        print("\nArray created successfully:")
        print(self.arr)

    def indexing_slicing(self):
        if self.arr is None:
            print("Create array first")
            return

        print("\nChoose an operation:")
        print("1. Indexing")
        print("2. Slicing")
        print("3. Go Back")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            row = int(input("Enter row index: "))
            col = int(input("Enter column index: "))
            print("Element =", self.arr[row][col])

        elif ch == 2:
            rs = int(input("Enter row start: "))
            re = int(input("Enter row end: "))
            cs = int(input("Enter column start: "))
            ce = int(input("Enter column end: "))

            print("\nSliced Array:")
            print(self.arr[rs:re, cs:ce])

    def math_operations(self):
        if self.arr is None:
            print("Create array first")
            return

        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        ch = int(input("Enter your choice: "))

        total = self.arr.size
        data = list(map(int, input(f"\nEnter same-size array elements ({total} values): ").split()))
        arr2 = np.array(data).reshape(self.arr.shape)

        print("\nOriginal Array:")
        print(self.arr)

        print("\nSecond Array:")
        print(arr2)

        if ch == 1:
            print("\nResult of Addition:")
            print(self.arr + arr2)

        elif ch == 2:
            print("\nResult of Subtraction:")
            print(self.arr - arr2)

        elif ch == 3:
            print("\nResult of Multiplication:")
            print(self.arr * arr2)

        elif ch == 4:
            print("\nResult of Division:")
            print(self.arr / arr2)

    def combine_split(self):
        if self.arr is None:
            print("Create array first")
            return

        print("\n1. Combine Arrays")
        print("2. Split Array")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            total = self.arr.size
            data = list(map(int, input(f"Enter {total} elements: ").split()))
            arr2 = np.array(data).reshape(self.arr.shape)

            print("\nCombined Array:")
            print(np.concatenate((self.arr, arr2)))

        elif ch == 2:
            n = int(input("Enter number of splits: "))
            print(np.array_split(self.arr, n))

    def search_sort_filter(self):
        if self.arr is None:
            print("Create array first")
            return

        print("\n1. Search")
        print("2. Sort")
        print("3. Filter")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            val = int(input("Enter value to search: "))
            print(np.where(self.arr == val))

        elif ch == 2:
            print(np.sort(self.arr))

        elif ch == 3:
            val = int(input("Show values greater than: "))
            print(self.arr[self.arr > val])

    def statistics(self):
        if self.arr is None:
            print("Create array first")
            return

        while True:
            print("\n========== Statistics Menu ==========")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Minimum")
            print("5. Maximum")
            print("6. Standard Deviation")
            print("7. Variance")
            print("8. Back")

            ch = int(input("Enter your choice: "))

            if ch == 1:
                print("Sum =", np.sum(self.arr))

            elif ch == 2:
                print("Mean =", np.mean(self.arr))

            elif ch == 3:
                print("Median =", np.median(self.arr))

            elif ch == 4:
                print("Minimum =", np.min(self.arr))

            elif ch == 5:
                print("Maximum =", np.max(self.arr))

            elif ch == 6:
                print("Standard Deviation =", np.std(self.arr))

            elif ch == 7:
                print("Variance =", np.var(self.arr))

            elif ch == 8:
                break

            else:
                print("Invalid Choice")


obj = DataAnalytics()

while True:
    print("\n====================================")
    print("Welcome to the NumPy Analyzer!")
    print("====================================")
    print("1. Create a NumPy Array")
    print("2. Indexing / Slicing")
    print("3. Perform Mathematical Operations")
    print("4. Combine or Split Arrays")
    print("5. Search, Sort, or Filter Arrays")
    print("6. Compute Statistics")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        obj.create_array()

    elif choice == 2:
        obj.indexing_slicing()

    elif choice == 3:
        obj.math_operations()

    elif choice == 4:
        obj.combine_split()

    elif choice == 5:
        obj.search_sort_filter()

    elif choice == 6:
        obj.statistics()

    elif choice == 7:
        print("\nThank You")
        break

    else:
        print("Invalid Choice")
