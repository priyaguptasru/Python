'''
Recursion:
Recursion involves a function calling itself directly or indirectly to solve a problem by breaking it down into simpler and more manageable parts. In Python, recursion is widely used for tasks that can be divided into identical subtasks.

Basic Structure of Recursive Function
def recursive_function(parameters):
    if base_case_condition:
        return base_result
    else:
        return recursive_function(modified_parameters)

Base Case: This is the condition under which the recursion stops. It is crucial to prevent infinite loops and to ensure that each recursive call reduces the problem in some manner.
Recursive Case: This is the part of the function that includes the call to itself. It must eventually lead to the base case. 
Example:
'''
# def factorial(n):
#     if n == 1:  #Base case
#         return 1
#     else:
#         return n * factorial(n-1) #Recursive case
# num=int(input("Enter the number: "))
# print(factorial(num))

'''Explanation of above code: The factorial of a number n (denoted as n!) is the product of all positive integers less than or equal to n. The recursive approach involves the function calling itself with a decremented value of n until it reaches the base case of 1.'''