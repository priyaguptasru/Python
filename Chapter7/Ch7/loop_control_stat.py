'''Loop Control Statements
Loop control statements change execution from their normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed. Python supports the following control statements:
continue
break
pass'''


'''Continue Statement
The continue statement in Python returns the control to the beginning of the loop.
Note: The continue statement is used to skip the current iteration of a loop and move to the next iteration. It is useful when we want to bypass certain conditions without terminating the loop.
Example:
'''
# for i in range(1, 11):
#     if(i==4): 
#         continue
#     print(i)
# #In above code, number from 1 to 3 will be print and when i=4, it will skip by the compiler and then again it will continue its work means then again it will print from 5 to 10


'''Break Statement
The break statement in Python brings control out of the loop.
Note: break statement is used to exit the loop prematurely when a specified condition is met.
Example:'''
# for i in range(1, 11):
#     if(i==4): 
#         break
#     print(i)
# #In above code, number from 1 to 3 will be print and when i=4, then loop will be breaked and terminated


'''Pass Statement
We use pass statement in Python to write empty loops. Pass is also used for empty control statements, functions and classes.
Note: It is a null statement in python. It instructs to "Do nothing
Example:'''
# for i in range(1, 11):
#     if(i==4): 
#         pass
#     print(i)
