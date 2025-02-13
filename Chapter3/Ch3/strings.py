'''Strings: 
One of the datatyps in python. 
It is a sequence of character(s) enclosed in a qoutes.
Python treats anything inside quotes as a string. This includes letters, numbers, and symbols. 
NOTES: Python has no character data type so single character is a string of length 1.
Strings in Python are immutable. This means that they cannot be changed after they are created. If we need to manipulate strings then we can use methods like concatenation, slicing, or formatting to create new strings based on the original.
We can primarily, write strings in below three ways:
Single qouted string--> var_name='Priya'
Double qouted string--> var_name="Priya"
Triple qouted string--> var_name=\'''Priya\'''
Example:
'''
# a="Priya"
# print(type(a))
# print(a)


'''Index of the string: Index is start from 0 to (length-1)
Example:priya
index of p=0
index of r=1
index of i=2
index of y=3
index of a=4

Negative index:Negative index can also be used in python. Index -1 is correspondent to (length-1), -2 is correspondent to (length-2) and so on..
Example:priya
index of p=0=-5
index of r=1=-4
index of i=2=-3
index of y=3=-2
index of a=4=-1
'''
# a='priyaGupta'
# print(a[5])
# print(a[-6])


'''Some methods/functions of Strings in python:'''

# # String lenght: It gives the lenght of the string
# # len(var_name)
# a='priyagupta'
# print(len(a)) #lenght= 10
# b='priya gupta'
# print(len(b)) #lenght=11 because white space is also counted in the string.


# # String slicing: For getting a part of the string
# # var_name[index1:index2] {NOTES: index1 is included and index2 is excluded}
# a='priyagupta'
# sl=a[1:4]
# print(sl)
# print(a[:4]) #This means a[first index:4] ie a[0:4]
# print(a[2:]) #This means a[2:(lenght)] ie a[2:5]
# # Slicing with skip value:For getting a part of string by skipping the value by the given numbers
# # var_name[index1:index2:skip_value] {NOTES: index1 is included and index2 is excluded and value will be skipped by the number of skip value }
# b='amitverma'
# print(b[2:7:2])
# print(b[:6:3]) #This means a[first index:6:3] ie a[0:6:3]
# print(b[3::1]) #This means a[3:(lenght):1] ie a[3:9:1]


# # String endswith: It tells whether the variable strings end with the mentioned string or not
# # endswith('req_str')
# a='priyagupta'
# print(a.endswith('pta')) #Return True as above string is ending with 'pta'
# print(a.endswith('iya')) #Return Flase as above string is ending with 'pta' and not 'iya'


# # String startswith: It tells whether the variable strings start with the mentioned string or not
# # startswith('req_str')
# a='priyagupta'
# print(a.startswith('pr')) #Return True as above string is starting with 'pr'
# print(a.startswith('iya')) #Return Flase as above string is starting with 'pr' and not 'iya'


# # String count: It count the total number of occurence of any character
# # count('req_char')
# a='priyagupta'
# print(a.count('a'))
# print(a.count('g'))


# # String capitalize: It return the string after capitalizing the first char of the string
# # capitalize()
# a='priyagupta'
# b='priya gupta'
# print(a.capitalize()) #Return 'Priyagupta
# print(b.capitalize()) #Return 'Priya gupta'. This means it capitalize only the first letter of the string


# # String find: It find the requested word in the string and return the index of the first char of that word
# # find(req_word)
# a='priyagupta'
# b='priya gupta'
# print(a.find('iya')) #Return index of i ie 2
# print(a.find('p')) #Return the index of first p only ie 0
# print(b.find(' ')) #Return the index of white space ie 5


# # String replace: This replace the old word with the new word in the entire string
# # replace('old_word' , 'new_word')
# a='priyagupta'
# print(a.replace('gupta' , 'verma'))
# print(a.replace('p' , 'x'))
