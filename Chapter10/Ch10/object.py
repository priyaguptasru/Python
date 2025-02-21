'''
Object:
An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data.
An object consists of:
State: It is represented by the attributes and reflects the properties of an object.
Behavior: It is represented by the methods of an object and reflects the response of an object to other objects.
Identity: It gives a unique name to an object and enables one object to interact with other objects.4

Creating Object:
Creating an object in Python involves instantiating a class to create a new instance of that class. This process is also referred to as object instantiation.
Example:
'''
class Dog:
    species = "Canine"
    def __init__(self, name, age):
        self.name = name 
        self.age = age

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3) #Creates an object of the Dog class with name as “Buddy” and age as 3.
print(dog1.name) #Accesses the instance attribute name of the dog1 object.
print(dog1.species) #Accesses the instance attribute spieces of the dog1 object.
print(dog1.age) #Accesses the instance attribute age of the dog1 object.
