#Single line comment.

'''Multi
line
comments'''

"""Multi
line
comments"""

# To comment and uncomment line or multi-lines in one go, select all the line(s) and press ctrl+/
# To bring the content in one line--> Alt+Z
# To copy the above line in next line--> Alt+Shift+DownArrow

'''Module: It is a file(s) containing codes which is usally written by someone else and onther can import it in his program and use it. 
Example of Module:Flask, Django, pyjokes, etc
There are 2 types of module in pyhton:
1) Built-in module: Pre installed modules in python. Eg: os, sys, math, datetime, etc.
2) External module: Need to install and import in our program. Eg: flask, pyjokes, etc.'''

'''Pip: It is a package manager for python. It is used to intall modules in our program.'''

'''To install any module using pip, use below command in terminal:
command: pip install module_name
Eg: pip install flask'''

'''to enter any further folder OR folders, use below command:
command: cd folder_name OR cd folder_path'''

'''to come out one folder back, use below command:
command: cd..'''

#example to use any module and import it in our program
#write a program to use pyjoke module(which print random jokes) in our program
''''firstly in terminal, install pyjokes module using below cmd. 
command: pip install pyjokes
and then import it in our program'''
import pyjokes
randomJoke= pyjokes.get_joke()
print(randomJoke)

'''REPL in python:
REPL stands for Read Evaluate Print Loop.
It’s an interactive shell that allows you to enter Python commands and directly see the results.
It is also known as interactive shell, interactive session, interpreter session, and REPL session.'''

'''How to enter and use REPL:
open window terminal of our system
type python and then press enter
you will find the REPL as a >>>
write your code
'''

'''Print Hello world in REPL:
Enter in REPL
print("Hello World")'''

'''How to use python as a calculator:
Enter in REPL
use it simply like you use calculator
Eg: 3+4
'''

'''How to use REPL for writing any code:
Enter in REPL
NOTES: to come one line down in the same progrom use shift+enter
       to run the program use enter
write your code in REPL. Eg:
>>> a=4
>>> b=2
>>> c=a/b
>>> print(c)
'''

