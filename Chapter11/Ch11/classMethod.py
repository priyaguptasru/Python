'''
Class Method in Python
A class method is a method that operates on the class level rather than on an instance. It is defined using the @classmethod decorator and takes cls (instead of self) as its first parameter.

Key Features of Class Methods:
It works with class variables (not instance variables).
It can be called using the class name or an instance.
It is commonly used for factory methods or modifying class attributes.

Example:
'''
class Employee:
    company = "Google"  # Class variable
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company  # Modifies the class variable
Employee.change_company("Microsoft") # Calling class method using class name
emp1 = Employee() # Creating an instance
print(emp1.company)  # Checking the updated company name
