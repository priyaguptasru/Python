'''Pass by Value and Pass by Reference in Python
Python’s argument-passing model is neither “Pass by Value” nor “Pass by Reference” but it is “Pass by Object Reference”. 
Depending on the type of object you pass in the function, the function behaves differently. Immutable objects show “pass by value” whereas mutable objects show “pass by reference”.

Example:
'''
# def call_by_value(x):
#     x = x * 2
#     print("in function value updated to", x)
#     return

# def call_by_reference(list):
#     list.append("D")
#     print("in function list updated to", list)
#     return

# my_list = ["E"]
# num = 6
# print("number before=", num) #print the original value ie 6
# call_by_value(num) #print after operating ie 12
# print("after function num value=", num) #the original value is not changed means print 6
# print("list before",my_list) #print the original value ir E
# call_by_reference(my_list) #print after operating ie E D
# print("after function list is ",my_list) #the original value is not changed means print E D

'''In the above code, we have shown how Python uses call by reference object concept in its program.
We pass an integer in function call_by_value(). Integers are immutable objects hence Python works according to call by value, and the changes made in the function are not reflected outside the function.
We then pass list to function by reference. In function call_by_reference() we pass a list that is an mutable object. Python works according to call by reference in this function and the changes made inside the function can also be seen outside the function.'''


'''
What is Pass by Reference In Python?
Pass by reference means that you have to pass the function (reference) to a variable, which means that the variable already exists in memory. 

What is Pass by Value In Python?
In this approach, we pass a copy of the actual variables in the function as a parameter. Hence any modification on parameters inside the function will not reflect in the actual variable.
'''