students = []

print("Welcome to the Student Data Organizer !")

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    
    if choice == "1":
        print("\nEnter student details:")

        student_id = input("Student ID: ")
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        birthdate = input("Date of Birth (YYYY-MM-DD): ")

        subjects_input = input("Subjects (comma-separated): ")
        subjects = set(sub.strip() for sub in subjects_input.split(","))

        student_tuple = (student_id, birthdate)

        student = {
            "id": student_tuple,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }

        students.append(student)
        print("Student added successfully !")

   
    elif choice == "2":
        print("\n--- Display All Students ---")

        if not students:
            print("No records found.")
        else:
            for s in students:
                print(f"Student ID: {s['id'][0]} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']} | Subjects: {', '.join(s['subjects'])}")

    
    elif choice == "3":
        sid = input("Enter Student ID to update: ")
        found = False

        for s in students:
            if s['id'][0] == sid:
                found = True
                print("1. Update Age")
                print("2. Update Subjects")
                ch = input("Enter choice: ")

                if choice == "1":
                    s['age'] = int(input("Enter new age: "))
                    print("Age updated!")

                elif choice == "2":
                    subjects_input = input("Enter new subjects: ")
                    s['subjects'] = set(sub.strip() for sub in subjects_input.split(","))
                    print("Subjects updated!")
                break

        if not found:
            print("Student not found!")

    
    elif choice == "4":
        sid = input("Enter Student ID to delete: ")
        found = False

        for i in range(len(students)):
            if students[i]['id'][0] == sid:
                del students[i]
                print("Student deleted!")
                found = True
                break

        if not found:
            print("Student not found!")

  
    elif choice == "5":
        all_subjects = set()

        for s in students:
            all_subjects.update(s['subjects'])

        print("\nUnique Subjects Offered:")
        for sub in all_subjects:
            print(sub)

   
    elif choice == "6":
        print("Thank you for using Student Data Organizer!")
        break

    else:
        print("Invalid choice! Try again.")