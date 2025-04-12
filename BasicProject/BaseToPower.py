'''Get an int value of base raises to the power of exponent
Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
Note here exp is a non-negative integer, and the base is an integer.
Example:
base = 5
exponent = 4
5 raises to the power of 4 is: 625 
i.e. (5 *5 * 5 *5 = 625)'''

def exponent(base, exp):
    res=base**exp
    print(f"{base} raise to {exp} is {res}")
b=int(input("Enter the base number: "))
e=int(input("Enter the exponent number: "))
exponent(b, e)