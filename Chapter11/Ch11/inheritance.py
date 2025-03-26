'''
Python Inheritance
Inheritance allows a class (child class) to acquire properties and methods of another class (parent class). It supports hierarchical classification and promotes code reuse.
'''

# Types of Inheritance:

# Single Inheritance: A child class inherits from a single parent class.
class Parent:
    def func1(self):
        print("This is Parent class")

class Child(Parent): #Inheriting property of class 'Parent'
    def func2(self):
        print("This is SingleParent Child class")

#Creating ojects and calling methods
print("Single Inheritance!!!")
obj1=Child()
obj1.func1()
obj1.func2()


# Multiple Inheritance: A child class inherits from more than one parent class.
class Parent1:
    def func3(self):
        print("This is Parent1 class")

class Parent2:
    def func4(self):
        print("This is Parent2 class")

class Child1(Parent1, Parent2):
    def func5(self):
        print("This is MultipleParents Child class")

print("\n\nMultiple Inheritance!!!")
obj2=Child1()
obj2.func3()
obj2.func4()
obj2.func5()


# Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another class.
class Parent3:
    def func6(self):
        print("This is Parent3 class")

class Child2(Parent3):
    def func7(self):
        print("This is Child of Parent3 class")

class Child3(Child2):
    def func8(self):
        print("This is Child of Child2 class")

print("\n\nMultilevel Inheritance!!!")
obj3=Child3()
obj3.func6()
obj3.func7()
obj3.func8()


# Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
class Parent4:
    def func9(self):
        print("This is Parent4 class")

class Child4(Parent4):
    def func10(self):
        print("This is Child of Parent4 class")

class Child5(Parent4):
    def func11(self):
        print("This is also Child of Parent4 class")

print("\n\nHierarchical Inheritance!!!")
obj4=Child4()
obj5=Child5()
obj4.func9()
obj4.func10()
obj5.func9()
obj5.func11()


# Hybrid Inheritance: A combination of two or more types of inheritance.
class Parent5(Child3, Child4): #Combination of multilevel and hierarchical
    def func12(self):
        print("This is Hybrid parent class")

print("\n\nHybrid Inheritance!!!")
obj6=Parent5()
obj6.func8()
obj6.func10()
obj6.func12()