'''
Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.
Given:
numbers_x = [10, 20, 30, 40, 10] ==> True
numbers_y = [75, 65, 35, 75, 30] ==> False
'''

n=int(input("Enter the length of the list: ")) #Take the lenght is the list
li=[] #Initialize the list with empty list
for i in range(n): #Enter the elements in the list
    ele= input(f'Enter element {i+1}: ')
    li.append(ele)
print(f"list: {li}") #Print the list
if(li[0] == li[n-1]): print(f"True! First and Last elements are same ie {li[0]}")
else: print(f"False! First element is {li[0]} and Last element is {li[n-1]}, hence not same.")