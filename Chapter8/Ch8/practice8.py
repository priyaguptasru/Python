# #P1: Write a program to find the  greatest of thre numbers using function
# def func_great(a,b,c):
#     if((a>=b) and (a>=c)):return a
#     elif((b>=a) and (b>=c)):return b
#     else:return c

# n1=int(input("Enter number 1: "))
# n2=int(input("Enter number 2: "))
# n3=int(input("Enter number 3: "))
# g=func_great(n1,n2,n3)
# print(f"Greatest number in {n1}, {n2}, {n3} is {g}")


# #P2: Write a program to convert celcius to farhenite using function
# def CelToFar(c):
#     f=(c*(9/5))+32
#     return f
# cel=int(input("Enter the celcius: "))
# print(f"Fahrenheit value is: {CelToFar(cel)}")


# #P3: How do you prevent a print() to print a new line at the end
# print("Hello")
# print("World")
# print("Hello", end='')
# print("World")
# # Using end='' in the print function


# #P4: Write a program to print the sum of n natural number using recursion.
# def rec_sum(n):
#     if(n==1):
#         return 1
#     else:
#         return (n + rec_sum(n-1))
# num=int(input("Enter the number: "))
# sum=rec_sum(num)
# print(sum)


# #P5: Write a program to convert inches to cms using function
# def incTOcm(i):
#     res=i*2.54
#     return res
# num=int(input("Enter the inches value: "))
# print(f"The value in cm is {incTOcm(num)}")


#P6: Write a python program to print the below pattern
'''
when n=3
***
**
*
'''
# n=int(input("Enter the number of line: "))
# for i in range(n, 0, -1):  # Loop from n down to 1
#     print("*"*i)


# #P7: Write a program to remove a given word from a list and strip it at the same time
# def remo(li, word):
#     n=[] #empty list
#     for item in li:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n

# my_list=["Priyaa", "Piyush", "Aamit",  "Snehaa"]
# print(remo(my_list,"aa"))