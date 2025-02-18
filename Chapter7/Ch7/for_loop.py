'''For Loop in Python:
For loops are used for sequential traversal. For example: traversing a list or string or array etc. In Python, there is “for in” loop which is similar to foreach loop in other languages. Let us learn how to use for loops in Python for sequential traversals with examples.

For Loop Syntax:
for iterator_var in sequence:
    statements

Range function in python:
It is used to generate a sequence of the number. We can also specify the start, stop and skip-size as follow:
range(start, stop, skip size)

Example:print the number from 1 to 10 using for loop    
'''
# for i in range(1, 11): #iterate till n-1
#     print(i)

# for i in range(1, 20, 2): #iterate till n-1 by skipping 2-2 numbers
#     print(i)

'''Example with List, Tuple, String, and Set, Dictionary Iteration Using for Loops in Python'''
# li=[1, 2.8, False, "Priya", 'a'] #list
# for i in li:print(i)
# tup=(1, 2.8, False, "Priya", 'a') #tuple
# for i in tup:print(i)
# str="priya" #string
# for i in str:print(i)
# se=set({1, 2.8, False, "Priya", 'a'}) #set
# for i in se:print(i)
# dic={"a":1, "b":2.8, "c":False, "d":"Priya", "e":'a'} #dict
# for i in dic:print(i, dic[i])


'''Iterating by the Index of Sequences:
We can also use the index of elements in the sequence to iterate. The key idea is to first calculate the length of the list and in iterate over the sequence within the range of this length.
Example:'''
# lis=[1, 2.8, False, "Priya", 'a'] 
# for i in range(len(lis)):print(lis[i])
'''Explanation: This code iterates through each element of the list using its index and prints each element one by one. The range(len(list)) generates indices from 0 to the length of the list minus 1.'''


'''Using else Statement with for Loop in Python
We can also combine else statement with for loop like in while loop. But as there is no condition in for loop based on which the execution will terminate so the else block will be executed immediately after for block finishes execution. 

Syntax:
for iterator_var in sequence:
    statements
else:
    statements

Example: print number from 1 to 10 using for loop and print DONE once completed    
'''
# for i in range(1, 11):print(i)
# else:print("DONE!!!")
'''Explanation: The code iterates through the list and prints each element. After the loop ends it prints “Inside Else Block” as the else block executes when the loop completes without a break.'''