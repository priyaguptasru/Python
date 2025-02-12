'''TypeCasting: Type Casting is the method to convert the Python variable datatype into a certain data type in order to perform the required operation by users.
There can be two types of Type Casting in Python:
Python Implicit Type Conversion
Python Explicit Type Conversion
'''

'''type(): type function is used to find thed data type of the given variable in the python.'''

'''Python Implicit Type Conversion: In this, method, Python converts the datatype into another datatype automatically.
Example:'''
# # Python automatically converts a to int 
# a = 7
# print(type(a)) 

# # Python automatically converts b to float 
# b = 3.0
# print(type(b)) 

# # Python automatically converts c to float as it is a float addition 
# c = a + b 
# print(c) 
# print(type(c))

# # Python automatically converts d to float as it is a float multiplication
# d = a * b
# print(d)
# print(type(d))

# # Python automatically converts e to boolean 
# e=True
# t=type(e)
# print(t)

# # Python automatically converts f to string 
# f='apple'
# print(type(f))

'''Python Explicit Type Conversion: In this method, Python needs user involvement to convert the variable data type into the required data type. 
Example:'''
# # User needs to convert one type to another as per his requirement
# a=5 #a is int type
# print('a=', a, 'and it is type of ', type(a))
# b=float(a) #here, a is converted to float type and stored in b
# print('b=', b, 'and it is type of ', type(b))
# c=str(a) #here, a is converted to str type and stored in c
# print('c=', c, 'and it is type of ',type(c))

# # User needs to convert one type to another as per his requirement
# a=5.3 #a is float type
# print('a=', a, 'and it is type of ', type(a))
# b=int(a) #here, a is converted to int type and stored in b
# print('b=', b, 'and it is type of ', type(b))
# c=str(a) #here, a is converted to str type and stored in c
# print('c=', c, 'and it is type of ',type(c))

# # User needs to convert one type to another as per his requirement
# # a='apple' #this type of str is not converted to both int and float
# # a='5.9' #this type of str is converted to only float and not int
# a='5' #this type of str is converted to both int and float
# print('a=', a, 'and it is type of ', type(a))
# b=int(a) #here, a is converted to int type and stored in b
# print('b=', b, 'and it is type of ', type(b))
# c=float(a) #here, a is converted to float type and stored in c
# print('c=', c, 'and it is type of ',type(c))

