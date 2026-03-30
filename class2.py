class Employee:
    
    def __init__(self, emp_id, name, age, salary):
        self.__emp_id = emp_id
        self._name = name
        self._age = age
        self._salary = salary

    def set_salary(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary

    def get_emp_id(self):
        return self.__emp_id

    def display(self):
        print(f"ID: {self.__emp_id}, Name: {self._name}, Age: {self._age}, Salary: {self._salary}")


class Manager(Employee):
    
    def __init__(self, emp_id, name, age, salary, department):
        super().__init__(emp_id, name, age, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")


class Developer(Employee):
    
    def __init__(self, emp_id, name, age, salary, language):
        super().__init__(emp_id, name, age, salary)
        self.language = language

    def display(self):
        super().display()
        print(f"Language: {self.language}")



employees = []

while True:
    print("\n1. Add Employee")
    print("2. Add Manager")
    print("3. Add Developer")
    print("4. Show Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = int(input("Enter Salary: "))

        employees.append(Employee(emp_id, name, age, salary))

    elif choice == "2":
        emp_id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = int(input("Enter Salary: "))
        department = input("Enter Department: ")

        employees.append(Manager(emp_id, name, age, salary, department))

    elif choice == "3":
        emp_id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = int(input("Enter Salary: "))
        language = input("Enter Language: ")

        employees.append(Developer(emp_id, name, age, salary, language))

    elif choice == "4":
        for emp in employees:
            print("------")
            emp.display()

    elif choice == "5":
        print("Exiting the system, all resources freed.")
        break

    else:
        print("Invalid choice")
        
        
        
class employee :
    def __init__(self,empid,name,age,salary):
        self.empid = empid
        self.name = name
        self.age = age
        self.salary = salary
        
        print("\nemployee created\n")
        
    def getinfo(self):
        print(f"\nemployee id : {self.empid} , name :{self.name} , age : {self.age} , salary :{self.salary}")
        
class manager(employee):
    def __init__(self,empid,name,age,salary,department):
        super().__init__(empid,name,age,salary)
        self.department = department
        
        print("\n manager created\n")
        
    def getinfo(self):
        super().getinfo()
        print(f"the manager is from {self.department} ! \n")
        
class developer(employee):
    def __init__(self,empid,name,age,salary,programming):
        super().__init__(empid,name,age,salary)
        self.programming = programming
        
    def getinfo(self):
        super().getinfo()
        print(f"the developer is expert of {self.programming} ! \n")
        
e_list = []
m_list = []
d_list = []

while True:
     
     print("enter 1 to employee") 
     print("enter 2 to manager") 
     print("enter 3 to developer") 
     print("enter 4 to view\n")
     
     choice = int(input("enter choice :"))
     
     match choice:
         case 1:
             id = len(e_list) + 1
             eobj = employee(id,"khushi",18,5679)
             e_list.append(eobj)
             
         case 2:
             id = len(m_list) + 1
             mobj = manager(id,"khushi",18,5679,"hr")
             m_list.append(mobj)
             
         case 3:
             id = len(d_list) + 1
             dobj = developer(id,"khushi",18,5679,"java")
             d_list.append(dobj)
        
         case 4:
            ch = int(input("enter 1,2,3 respectively for ee,man,dev :"))
            
            if ch==1:
                for e in e_list:
                    e.getinfo()
            elif ch==2:
                for m in m_list:
                    m.getinfo()
            elif ch==3:
                for d in d_list:
                    d.getinfo()
            else:
                print("choice is wtong")
                    
            