'''
Python Polymorphism:
Polymorphism allows methods to have the same name but behave differently based on the object’s context. It can be achieved through method overriding or overloading.

Types of Polymorphism:
Compile-Time Polymorphism
Run-Time Polymorphism
'''

# Compile-Time Polymorphism: This type of polymorphism is determined during the compilation of the program. It allows methods or operators with the same name to behave differently based on their input parameters or usage. It is commonly referred to as method or operator overloading.
# In Python, compile-time polymorphism (also known as method overloading) is not natively supported like in Java or C++, because Python does not allow multiple methods with the same name in a class. However, we can achieve similar behavior using default arguments or variable-length arguments (*args and **kwargs).


# Run-Time Polymorphism: This type of polymorphism is determined during the execution of the program. It occurs when a subclass provides a specific implementation for a method already defined in its parent class, commonly known as method overriding.
# Runtime polymorphism is achieved in Python using method overriding in inheritance. This means that a subclass provides a specific implementation of a method that is already defined in its parent class.
class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def make_sound(self):  # Overriding parent class method
        print("Dog barks")

class Cat(Animal):
    def make_sound(self):  # Overriding parent class method
        print("Cat meows")


# # Creating objects of subclasses
# animal1 = Dog()
# animal2 = Cat()

# # Calling the overridden method (Runtime Polymorphism)
# animal1.make_sound()  # Output: Dog barks
# animal2.make_sound()  # Output: Cat meows


# # Using Runtime Polymorphism with a Loop:
# animals = [Dog(), Cat(), Animal()]

# for animal in animals:
#     animal.make_sound()  # Calls the appropriate overridden method
