class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.__emp_id = emp_id
        self.name = name
        self.age = age
        self.__salary = salary

        print("\nEmployee created\n")

    def getInfo(self):
        print(f"ID: {self.__emp_id}, Name: {self.name}, Age: {self.age}, Salary: {self.__salary}")


class Manager(Employee):
    def __init__(self, emp_id, name, age, salary, department):
        super().__init__(emp_id, name, age, salary)
        self.department = department

        print("\nManager created\n")

    def getInfo(self):
        super().getInfo()
        print(f"Department: {self.department}\n")


class Developer(Employee):
    def __init__(self, emp_id, name, age, salary, programming):
        super().__init__(emp_id, name, age, salary)
        self.programming = programming

        print("\nDeveloper created\n")

    def getInfo(self):
        super().getInfo()
        print(f"Programming Language: {self.programming}\n")


e_list = []
m_list = []
d_list = []

while True:
    print("\n1. Add Employee")
    print("2. Add Manager")
    print("3. Add Developer")
    print("4. Show Details")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    match choice:
        case 1:
            id = len(e_list) + 1
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            salary = int(input("Enter salary: "))

            eobj = Employee(id, name, age, salary)
            e_list.append(eobj)

        case 2:
            id = len(m_list) + 1
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            salary = int(input("Enter salary: "))
            dept = input("Enter department: ")

            mobj = Manager(id, name, age, salary, dept)
            m_list.append(mobj)

        case 3:
            id = len(d_list) + 1
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            salary = int(input("Enter salary: "))
            prog = input("Enter programming language: ")

            dobj = Developer(id, name, age, salary, prog)
            d_list.append(dobj)

        case 4:
            ch = int(input("Enter 1=Employee, 2=Manager, 3=Developer: "))

            if ch == 1:
                for e in e_list:
                    e.getInfo()
            elif ch == 2:
                for m in m_list:
                    m.getInfo()
            elif ch == 3:
                for d in d_list:
                    d.getInfo()
            else:
                print("Wrong choice")

        case 5:
            print("Exiting...")
            break

        case _:
            print("Invalid choice")