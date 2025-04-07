'''Write a Python code to accept a string from the user and display characters present at an even index number.
For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.'''

ch=input("Enter any string: ")
print(f'Characters present at an even index in string "{ch}" are:')

# #method 1: Using for loop
# for i in range(0, len(ch), 2):
#     print(ch[i])

#method 2: Using list slicing
# x=list(ch)
# for i in x[0::2]:
#     print (i)