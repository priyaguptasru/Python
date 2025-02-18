# #P1: Print a table of number n using for loop
# num=int(input("Enter number: "))
# for i in range(1, 11):print(f"{num} * {i} = {num*i}")


#P2: Print a table of number n using while loop
# num=int(input("Enter number: "))
# i=0
# while(i<10):
#     i=i+1
#     print(f"{num} * {i} = {num*i}")


# #P3: Write a program to greet all the persons whose name is starts from "S" in the below list
# '''list_name=["Priya", "Sunny", "Soumya", "Amit", "Piyush", "Sneha"]'''
# list_name=["Priya", "Sunny", "Soumya", "Amit", "Piyush", "Sneha"]
# for name in list_name:
#     if name.startswith("S"):
#         print(f"Hello {name} !!!")


# #P4: Write a program to check if the number is prime or not.
# num=int(input("Enter the number: "))
# for i in range(2, num-1):
#     if(num%i==0):
#         print("Number is not prime.")
#         break
# else:print("Number is prime.")


# #P5: Write a program to find the sum of n natural numbers using while loop
# num=int(input("Enter number: "))
# i=0
# sum=0
# while(i<num):
#     i=i+1
#     sum=sum+i
# print(sum)


# #P6: Write a program to find the factorial of numbre using for loop
# num=int(input("Enter number: "))
# product=1
# for i in range(1, num+1):
#     product=product*i
# print(product)


# #P7:Write a python program to print the below pattern
# '''
# when n=3
#   *
#  ***
# *****
# '''
# # n=int(input("Enter the number of line: "))
# # for i in range(1, n+1):
# #     print(' ' * (n-i), end='') #print(end='')-->It do not add new line by efault
# #     print('*' * (2*i-1), end='')
# #     print()

# #OR

# # n=int(input("Enter the number of line: "))
# # for i in range(1, n + 1): print((' ' * (n - i)) + ('*' * (2 * i - 1)))


# #P8:Write a python program to print the below pattern
# '''
# when n=3
# *
# **
# ***
# '''
# n=int(input("Enter the number of line: "))
# for i in range(1, n + 1): print('*'*i)


# #P9:Write a python program to print the below pattern
# '''
# when n=3 
# ***
# * *
# ***
# '''
# n = int(input("Enter the number of lines: "))
# for i in range(1, n + 1):                 # Loop from 1 to n (inclusive)
#     if i == 1 or i == n:                  # First or last row
#         print('*' * n)                    # Print n stars
#     else:                                 # Middle rows
#         print('*', end='')                # Left border star
#         print(' ' * (n - 2), end='')      # Spaces in between
#         print('*')                        # Right border star


#P10: Write a program to print the multiplication table of number n in reverse order.
# n=int(input("Enter the number: "))
# i=11
# while(i>1):
#     i=i-1
#     print(f"{n} * {i} = {n*i}")