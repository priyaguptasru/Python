'''while loop:
In Python, a while loop is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the line immediately after the loop in the program is executed.

While Loop Syntax:
while (expression):
    statements

Example: print number from 1 to 10 using while loop
'''
# i=0
# while(i<10):
#     i=i+1
#     print(i)


'''Using else statement with While Loop in Python
Else clause is only executed when our while condition becomes false. If we break out of the loop or if an exception is raised then it won’t be executed.

Syntax of While Loop with else statement:
while condition:
     # execute these statements
else:
     # execute these statements

Example:print number from 1 to 10 using while loop and print DONE once completed
'''
# i=0
# while(i<10):
#     i=i+1
#     print(i)
# else:print("DONE!!!")    


'''Infinite While Loop in Python
If we want a block of code to execute infinite number of times then we can use the while loop in Python to do so.
Note: It is suggested not to use this type of loop as it is a never-ending infinite loop where the condition is always true and we have to forcefully terminate the compiler.
'''