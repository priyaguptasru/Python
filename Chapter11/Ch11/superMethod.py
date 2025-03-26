'''
Super():
In Python, the super() function is used to refer to the parent class or superclass. It allows you to call methods defined in the superclass from the subclass, enabling you to extend and customize the functionality inherited from the parent class.

Syntax of super() in Python
Syntax: super()
Return : Return a proxy object which represents the parent’s class.

Why is the super() Method Needed in Python?
The super() method is used in Python to call methods from the parent class inside a child class. It is especially useful in inheritance when a subclass needs to extend or modify the behavior of its parent class without completely overriding it.
Key Reasons to Use super():
Access Parent Class Methods: Allows calling methods from the parent class without directly referencing the class name.
Avoid Code Duplication: Helps reuse existing code from the parent class, reducing redundancy.
Support Multiple Inheritance: Works well when dealing with multiple base classes.
Maintainable and Scalable Code: If the parent class name changes, super() ensures that child classes still work correctly.
Example:
'''
# # Using super() to Call Parent Class Method
# class Parent:
#     def show(self):
#         print("This is the Parent class method.")
# class Child(Parent):
#     def show(self):
#         super().show()  # Calling parent class method
#         print("This is the Child class method.")
# obj = Child() # Creating an object of Child class
# obj.show()
'''
 Explanation:
super().show() calls the show() method from the Parent class before executing the child class’s method.
This ensures the parent class method runs before or along with the overridden method.
'''

# Using super() in __init__()
class Employee: #Parent/Base Class
    def __init__(self, Name, ID, Address):
        self.Name=Name
        self.ID=ID
        self.Address=Address
class Company(Employee): #Child/Derived Class
    comp="Microsoft"
    def details(self, Name, ID, Address, Language):
        super().__init__(Name, ID, Address) #calling the method of Parent class
        self.Language=Language
e1=Company("Priya", 1234, "Salempur")
e1.details("Priya", 1234, "Salempur", "Python")
print(f"{e1.comp} {e1.Name} {e1.ID} {e1.Address} {e1.Language}")


'''Using super() helps to reuse code, avoid redundancy, and maintain the structure of inheritance properly. It’s especially useful when working with multiple inheritance or when a subclass wants to modify but still use functionality from its parent class.'''