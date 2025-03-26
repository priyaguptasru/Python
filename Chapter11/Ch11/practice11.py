# #P1: Create a class TwoDVector and used it to creating a another class representing a ThreeDVector class
# class TwoDVector:
#     def __init__(self, i, j):
#         self.i=i
#         self.j=j
#     def show(self):
#         print(f'The 2D vector is {self.i}i {self.j}j')
# class ThreeDVector(TwoDVector):
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.k=k
#     def show(self):
#         print(f'The 3D vector is {self.i}i {self.j}j {self.k}k')
# two=TwoDVector(1,2)
# two.show()
# three=ThreeDVector(4,5,6)
# three.show()


# #P2: Create a class Pet from a class Animal and further create class Dog from Pet. Add a method bark to a class Dog
# class Animal:
#     def show(self):
#         print("I am animal.")
# class Pet(Animal):
#     def show(self):
#         super().show()
#         print("I am pet.")
# class Dog(Pet):
#     def bark(self):
#         print("I am dog.")
# d=Dog()
# d.show()
# d.bark()


# #P3: Create a class Employee and add salary and increment properties to it. Write a method SalaryAfterIncrement with a @property decorator with a setter which changes the value of increment based on the salary.
# class Employee:
#     salary=120000
#     increment=20
#     # print(f'Salary= {salary}')
#     # print(f'Increment percentage= {increment}')
#     @property
#     def SalaryAfterIncrement(self):
#         return (self.salary + self.salary * (self.increment/100))
#     @SalaryAfterIncrement.setter
#     def SalaryAfterIncrement(self, salary):
#         self.increment=((salary/self.salary)-1)*100
# e=Employee()
# # print(f'Salary after increment= {e.SalaryAfterIncrement}')
# e.SalaryAfterIncrement=124000
# print(f'Increment= {e.increment}')
'''
The @property decorator in Python is used to define a method as a property, allowing controlled access to class attributes without explicitly calling a method. It is mainly used for encapsulation (hiding data) and creating computed properties.

The @setter decorator in Python is used along with @property to allow modification of a property value in a controlled way. It is used to define a setter method for a property, ensuring validation, constraints, or computed updates when assigning a value.
'''

# #P4: Write a class Complex to represent complex numbers, along with overloaded operators + and * which adds and multiply them.
# class Complex:
#     def __init__(self, real, imag):
#         self.real = real 
#         self.imag = imag 
#     def __add__(self, other):
#         return Complex(self.real + other.real, self.imag + other.imag)
#     def __mul__(self, other):
#         real_part = (self.real * other.real) - (self.imag * other.imag)
#         imag_part = (self.real * other.imag) + (self.imag * other.real)
#         return Complex(real_part, imag_part)
#     def __str__(self):
#         return f"{self.real} + {self.imag}i"
# c1 = Complex(3, 2)
# c2 = Complex(1, 7)

# # Adding complex numbers
# c3 = c1 + c2  # Uses overloaded + operator
# print(f"Addition: {c3}")  # Output: 4 + 9i

# # Multiplying complex numbers
# c4 = c1 * c2  # Uses overloaded * operator
# print(f"Multiplication: {c4}")  # Output: -11 + 23i
'''
The __str__ method in Python is a special (dunder) method used to return a human-readable string representation of an object. It is automatically called when you use print() or str() on an instance of the class.
'''

# #P5: Write a class vector representing a vector of n dimensions. Overload the + and *  operators which calculate the sum and the dot product of them.
# class Vector:
#     def __init__(self, components):
#         """Initialize a vector with a list of components"""
#         self.components = components
#     def __add__(self, other):
#         """Overloads + operator for vector addition"""
#         if len(self.components) != len(other.components):
#             raise ValueError("Vectors must have the same dimensions for addition.")
#         result = [a + b for a, b in zip(self.components, other.components)]
#         return Vector(result)
#     def __mul__(self, other):
#         """Overloads * operator for dot product"""
#         if len(self.components) != len(other.components):
#             raise ValueError("Vectors must have the same dimensions for dot product.")
#         result = sum(a * b for a, b in zip(self.components, other.components))
#         return result  # Returns a scalar (not a Vector)
#     def __str__(self):
#         """String representation of the vector"""
#         return f"Vector({self.components})"
# # Creating vector objects
# v1 = Vector([1, 2, 3])
# v2 = Vector([4, 5, 6])
# # Performing vector addition
# v3 = v1 + v2
# print(f"Vector Addition: {v3}")  # Output: Vector([5, 7, 9])
# # Performing dot product
# dot_product = v1 * v2
# print(f"Dot Product: {dot_product}")  # Output: 32


# #P6: Write a __str__() method to print the vector as follow:
# # 7i+8j+10k
# # Asume the vector of dimension 3 for this problem.
# class Vector:
#     def __init__(self, components):
#         """Initialize a 3D vector with a list of 3 components"""
#         if len(components) != 3:
#             raise ValueError("This Vector class only supports 3D vectors.")
#         self.components = components
#     def __add__(self, other):
#         """Overloads + operator for vector addition"""
#         result = [a + b for a, b in zip(self.components, other.components)]
#         return Vector(result)
#     def __mul__(self, other):
#         """Overloads * operator for dot product"""
#         result = sum(a * b for a, b in zip(self.components, other.components))
#         return result  # Returns a scalar (dot product)
#     def __str__(self):
#         """String representation in the format 'xi + yj + zk'"""
#         return f"{self.components[0]}i + {self.components[1]}j + {self.components[2]}k"
# # Creating vector objects
# v1 = Vector([3, 4, 5])
# v2 = Vector([4, 1, 2])
# # Performing vector addition
# v3 = v1 + v2
# print(f"Vector Addition: {v3}")  # Output: 7i + 5j + 7k
# # Performing dot product
# dot_product = v1 * v2
# print(f"Dot Product: {dot_product}")  # Output: 22


# #P7: Override the __len__() on vector of problem 5 to display the dimension of the vector.
# class Vector:
#     def __init__(self, components):
#         """Initialize a vector with a list of components"""
#         if not components:
#             raise ValueError("Vector cannot be empty.")
#         self.components = components
#     def __add__(self, other):
#         """Overloads + operator for vector addition"""
#         if len(self.components) != len(other.components):
#             raise ValueError("Vectors must have the same dimensions for addition.")
#         result = [a + b for a, b in zip(self.components, other.components)]
#         return Vector(result)
#     def __mul__(self, other):
#         """Overloads * operator for dot product"""
#         if len(self.components) != len(other.components):
#             raise ValueError("Vectors must have the same dimensions for dot product.")
#         result = sum(a * b for a, b in zip(self.components, other.components))
#         return result  # Returns a scalar (dot product)
#     def __str__(self):
#         """String representation of the vector in 'xi + yj + zk' format"""
#         terms = [f"{c}e{i+1}" for i, c in enumerate(self.components)]
#         return " + ".join(terms)
#     def __len__(self):
#         """Returns the dimension of the vector"""
#         return len(self.components)
# # Creating vector objects
# v1 = Vector([1, 2, 3])
# v2 = Vector([4, 5, 6, 7])
# # Performing vector addition
# v3 = v1 + v2  # This will raise an error (different dimensions)
# print(f"Vector Addition: {v3}")
# # Performing dot product
# dot_product = v1 * v2
# print(f"Dot Product: {dot_product}")
# # Checking dimensions
# print(f"Dimension of v1: {len(v1)}")  # Output: 3
# print(f"Dimension of v2: {len(v2)}")  # Output: 4
