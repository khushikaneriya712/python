print("  Welcome to Pattern Generator & Number Analyzer ")

while True:
    print("\nSelect an Option:")
    print("1. Generate a Pattern")
    print("2. Analyze Range of Numbers")
    print("3. Exit")
    
    choice = input("Enter your choice : ")
    
    if choice == "1":
        while True:
            rows = int(input("Enter the number of rows of pattern : "))
            
            if rows <= 0:
                print("Invalid row count! Must be positive.")
                break
            else:
                print("\nGenerated Pattern:\n")
                
                for i in range(1, rows + 1):
                    for j in range(i):
                        print("*", end=" ")
                    print()
                break

    elif choice == "2":
        while True:
            start = int(input("Enter the start num of range: "))
            end = int(input("Enter the end num of range : "))
            
            if end <= start:
                print("Invalid range! End number must be greater than start.")
                continue
            else:
                break
        
        total_sum = 0
        
        for num in range(start, end + 1):
            
            if num % 2 == 0:
                print(num, "is Even")
            else:
                print(num, "is Odd")
            
            total_sum += num
        
        print("\nSum of all numbers =", total_sum)

    elif choice == "3":
        print("Exiting the program Goodbye!!")
        break
    
    else:
        print("Invalid choice! Please select 1, 2 or 3.")