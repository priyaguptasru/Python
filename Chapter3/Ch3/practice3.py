# #P1: Write a program to display a user entered name followed by Good Afternoon using input()
# name=input("Enter the name: ")
# # print("Good Afternoon", name, "!!!")
# print(f"Good Afternoon {name} !!!")
'''f-string: Python offers a powerful feature called f-strings (formatted string literals) to simplify string formatting and interpolation. f-strings is introduced in Python 3.6 it provides a concise and intuitive way to embed expressions and variables directly into strings. The idea behind f-strings is to make string interpolation simpler. '''


# #P2: Write a program to fill in a letter template given below with name and date
# '''
# letter=Dear <Name>
#        You are selected!
#        <Date>
# '''
# name=input("Enter name: ")
# date=input("Enter date: ")
# letter='''Dear <Name>
#        You are selected!
# <Date>'''
# print(letter.replace('<Name>' , name).replace('<Date>' , date))


# #P3: Write a program to detect double space in a string
# a='priya  amit gupta verma'
# b='priya amit gupta verma'
# print(a.find("  "))
# print(b.find("  ")) #Return -1 as there is not double space


# #P4: Replace a double space with a single space of problem P3
# a='priya  amit gupta verma'
# print(a.replace("  ", " "))


# #P5:Write a program to format the below string using Escape Sequence Character
# '''
# letter="Dear Priya,You are learning Python. Thanks!"
# '''
# print("Dear Priya,\n\tYou are learning Python. \nThanks!")