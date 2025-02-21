# #P1: Create a class 'Programmer' for storing information of few employees working at Microsoft.
# class Programmer:
#     company="Microsoft"
#     def __init__(self, name, empid, salary):
#         self.name=name
#         self.empid=empid
#         self.salary=salary
# # e1=Programmer("Priya", 123, 1200000)
# name=input("Enter name: ")
# empid=int(input("Enter empid: "))
# salary=int(input("Enter salary: "))
# e1=Programmer(name, empid, salary)
# print(f'\nName= {e1.name}\nEmpID= {e1.empid}\nSalary= {e1.salary}\nCompany= {e1.company}')   


# #P2: Write a class 'Calculator' capable of finding square, cube and squareroot of a number
# class Calculator:
#     def __init__(self, n):
#         self.n=n
#     def square(self):
#         print(f'Square of {self.n} is {self.n**2}')
#     def cube(self):
#         print(f'Cube of {self.n} is {self.n**3}')
#     def squareroot(self):
#         print(f'Squareroot of {self.n} is {self.n**0.5}')
# num=int(input("Enter a number: "))
# cal=Calculator(num)
# cal.square()
# cal.cube()
# cal.squareroot()


# #P3: Create a class with class attribute 'a' and create a object from it and set 'a' directly using object.a=0 . Does this change the class attribute?
# class Attribute: #class
#     a=1 #class attribute
#     print(a) #print the value of class attribute as it is in class ie 1
# obj=Attribute() #creating object of the class
# obj.a=0 #object attribute
# print(obj.a) #print the value of object attribute as it is calling object attribute ie 0
# print(Attribute.a) #print the value of class attribute as it is calling class attribute ie 1
# # Hence class attribute will not affected by chaning the value of object attributes.


# #P4: Add a static method in P1 to greet the user with 'Hello buddy!!!\nBelow are your details'
# class Programmer:
#     company="Microsoft"
#     def __init__(self, name, empid, salary):
#         self.name=name
#         self.empid=empid
#         self.salary=salary
#     @staticmethod
#     def hello():
#         print(f"\nHello buddy!!!\nBelow are your details.")
# e1=Programmer("Priya", 123, 1200000)
# e1.hello()
# print(f'Name= {e1.name}\nEmpID= {e1.empid}\nSalary= {e1.salary}\nCompany= {e1.company}\n')
# e2=Programmer("Amit", 321, 2400000)
# e2.hello()
# print(f'Name= {e2.name}\nEmpID= {e2.empid}\nSalary= {e2.salary}\nCompany= {e2.company}')

'''
Static Method in Python
A static method in Python is a method inside a class that does not depend on the instance (object) of the class. It is defined using the @staticmethod decorator and does not take self or cls as the first argument.
Key Features of Static Methods:
They belong to the class, not to an instance.
They cannot modify class or instance attributes.
They behave just like regular functions but are inside a class for better organization.
'''


# #P5: Write a class Train which has a method to book a ticket, get running status  and fare info of a train running under Indian Railway
# from random import randint
# class Train:
#     trainnumber=randint(10000, 99999)
#     def bookticket(self, trainno, fro, to):
#         print(f"\nTicket is successfully booked for Train number:{self.trainnumber} from {fro} to {to}")
#     def runningstatus(self, trainno):
#         print(f'Train number:{self.trainnumber} is running on time.')
#     def fareinfo(self, trainno, fro, to):
#         print(f'Ticket fare for Train number:{self.trainnumber} from {fro} to {to} is Rs{randint(100, 1000)}\n')
# t=Train()
# tn=Train.trainnumber
# t.bookticket(tn, "Salempur", "Mau")
# t.runningstatus(tn)
# t.fareinfo(tn, "Salempur", "Mau")/


#P6: Is it possible to change the self parameter inside the class to something else(say priya). Try changing self to priya and see the effect.
'''
Yes, You Can Change self to Any Other Name (e.g., priya)!
The self parameter in Python is just a convention. You can replace it with any other name, and the program will still work. However, using self is a best practice for readability and maintainability.
Example:
'''
# class Person:
#     def __init__(priya, name, age):  # Using 'priya' instead of 'self'
#         priya.name = name
#         priya.age = age
#     def display(priya):
#         print(f"Name: {priya.name}, Age: {priya.age}")
# # Creating an object
# p = Person("Amit", 25)
# # Calling the method
# p.display()
'''
Explanation:
priya replaces self in all instance methods.
It still works correctly because Python only requires a reference to the instance, not a specific keyword.
However, it is not recommended because self is the widely accepted standard.
'''