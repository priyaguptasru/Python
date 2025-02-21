'''
Class:
A class is a collection of objects. 
Classes are blueprints for creating objects. 
A class defines a set of attributes and methods that the created objects (instances) can have.
Classes are created by keyword class.
Attributes are the variables that belong to a class.
Attributes are always public and can be accessed using the dot (.) operator. Example: Myclass.Myattribute

Creating a class:
Example:
'''
class Dog: # Class named as Dog
    species = "Canine"  # Class attribute shared by all instances of the class.

    def __init__(self, name, age): #Initializes the name and age attributes when a new object is created.
        self.name = name  # Instance attribute 
        self.age = age  # Instance attribute


#Example:
class Employee: #Class
    name= "Priya" #Class attributes
    langauge= "Python"
    salary= "2400000"
emp=Employee() #Creating object of the class
print(f"{emp.name}\n{emp.langauge}\n{emp.salary}")


'''
Self Parameter:
self parameter is a reference to the current instance of the class. It allows us to access the attributes and methods of the object.
Example:
'''
class Dog: #Class
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Refers to the name attribute of the object (dog1) calling the method.
        self.age = age  # Refers to the age attribute of the object (dog1) calling the method.

dog1 = Dog("Buddy", 3)  # Create an instance of Dog
dog2 = Dog("Charlie", 5)  # Create another instance of Dog

print(dog1.name, dog1.age, dog1.species)  # Access instance and class attributes
print(dog2.name, dog2.age, dog2.species)  # Access instance and class attributes
print(Dog.species)  # Access class attribute directly


'''
__init__ Method:
__init__ method is the constructor in Python, automatically called when a new object is created. It initializes the attributes of the class.
Example:
'''
class Dog:
    def __init__(self, name, age): #__init__ is a special method used for initialization.
        self.name = name #Instance attributes initialized in the constructor.
        self.age = age #Instance attributes initialized in the constructor.

dog1 = Dog("Buddy", 3)
print(dog1.name, dog1.age)  
