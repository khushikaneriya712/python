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
                    
            