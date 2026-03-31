print("welcome to the interactive personal data collecter !")
print()

name=input("please enter your name :")
age=input("please enter your age :")
height=input("please enter your height :")
favouritenumber=input("please enter your favourite number :")
print()

print("thank you! here is the information we collected:")
print()

print("name :",name,("type:",type(name),"memory address :",id(name)))
print("age :",age,("type :",type(age),"memory address :",id(age)))
print("height :",height,("type :",type(height),"memory address :",id(height)))
print("favouritenumber :",favouritenumber,("type :",type(favouritenumber),"memory address :",id(favouritenumber)))

print()

current_year = 2026


print("your birth year is approximately :",("based on yur age of ",age))
print()

print("thank you for using the personal data collector. goodbye !")