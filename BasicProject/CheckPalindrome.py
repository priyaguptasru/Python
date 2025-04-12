'''Write a Python code to check if the given number is palindrome. A palindrome number is a number that is the same after reverse. For example, 545 is the palindrome number.
Expected Output:
original number 121
Yes. given number is palindrome number
original number 125
No. given number is not palindrome number'''

#For number:
n=int(input("Enter the number: "))
rev=int(str(n)[::-1]) #There’s no direct built-in for reversing a number, but you can convert it to a string, reverse it, then convert it back: str(n)=>converting a number n to string; [::-1]=>using slicing method to convert the string; int()=>converting it back to  interger.
if(n == rev): print("Yes, given number is palindrome.")
else: print("No, given number is not palindrome.")

# #For string
# n=input("Enter your input: ")
# rev=''.join(reversed(n))
# if(n == rev): print("Yes, given input is palindrome.")
# else: print("No, given input is not palindrome.")