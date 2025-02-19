'''Functions in pyhton:
Python Functions is a block of statements that return the specific task. The idea is to put some commonly or repeatedly done tasks together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.

Some Benefits of Using Functions
Increase Code Readability 
Increase Code Reusability

Function Declaration in pyhton:
Syntax:
def func_name(parameters):
    statements

Example:
'''
# def fun1(): #defined a function with function name fun1
#     print("Hello World!!") #the above function will perform this task


'''
Types of Functions in Python
Below are the different types of functions in Python:
Built-in library function: These are Standard functions in Python that are available to use.
User-defined function: We can create our own functions based on our requirements.
'''


'''
Calling a function in python:
After creating a function in Python we can call it by using the name of the functions Python followed by parenthesis containing parameters of that particular function.

Syntax of function call:
Syntax:
def func_name():
    statements
func_name() #calling a function

Example:
'''
# def fun1(): #defined a function with function name fun1
#     print("Hello World!!") #the above function will perform this task
# fun1() #called the function to perform and provide the output


'''
Function with an arguments:
A function can accepts some values it can works with. We can put this values in the paranthesis.

Syntax:
def func_name(parameters):
    statements
    return expression
func_name(values)

Example:
'''
# def func_sum(a, b):
#     c=a+b
#     print(c)
# func_sum(3, 5)
# func_sum(4, 9)
# func_sum(1, 3)


# def func_sum(a, b):
#     c=a+b
#     return c
# n1=int(input("Enter number 1: "))
# n2=int(input("Enter number 2: "))
# # res= func_sum(n1, n2)
# # print(res)
# print(func_sum(n1, n2))


'''
Default parameter values:
We can have a value as default argument in the function and this value is used when no argument are passed.

Syntax:
def func_name(parameters="default value"):
    statements
    return expression
func_name()

Example:
'''
# def func_sum(a, b=9):
#     c=a+b
#     print(c)
# func_sum(3, 5) #here a=3 and b=5
# func_sum(4) #here, a=4 and this will take by default value of b ie 9 which is taken in func