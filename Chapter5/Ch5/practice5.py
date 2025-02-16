# #P1: Write a program to create a dictonary of  Hindi words with its meaning in English. Provide user with an option to look it up
# words={
#     "Kursi": "Chair",
#     "Mez": "Table",
#     "Aam": "Mango",
#     "Madad": "Help",
#     "Kaam": "Work"
# }
# translate=input("Enter the word: ")
# print(words.get(translate))


# #P2: Write a program to input eight numbers from the user and display all the unique numbers
# s=set()
# i=int(input("Enter number1: "))
# s.add(i)
# i=int(input("Enter number2: "))
# s.add(i)
# i=int(input("Enter number3: "))
# s.add(i)
# i=int(input("Enter number4: "))
# s.add(i)
# i=int(input("Enter number5: "))
# s.add(i)
# i=int(input("Enter number6: "))
# s.add(i)
# i=int(input("Enter number7: "))
# s.add(i)
# i=int(input("Enter number8: "))
# s.add(i)
# print(s)


# #P3: Can we have a set with 18(int) and "18"(str) a value in it?
# s=(18, "18")
# print(s)
# # Python treats 18 (int) and "18" (str) as different types, and therefore, they are not considered the same element. Hence it will display both the elements


# #P4: What will the length of the following below set
# '''
# s=set()
# s.add(2)
# s.add(2.0)
# s.add("2")
# '''
# s=set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(s)
# print(len(s))
# # In Python, the set s will contain three elements, but the behavior depends on how Python handles different data types: 2 (int) and 2.0 (float) are considered the same value. Although one is an integer and the other a float, Python treats them as equivalent because they represent the same number (2), so they are not added as distinct elements in the set. And "2" (str) is a string and is completely different from the integer 2 or the float 2.0, so it will be treated as a separate element. Therefore, the set s will only have two distinct elements: 2 (either as int or float) and "2" (string). So, the length of the set s will be 2.


# #P5: s={} ;here what is the type of s?
# s={} #It is empty dict
# print(type(s)) #Return dict


# #P6: Create an empty dictionary. Allow 4 friends to enter their favorite language as a value and use key as their names. Assume that the names are unique
# d={}
# name=input("Enter name1: ")
# lang=input("Enter his fav lang: ")
# d.update({name:lang})
# name=input("Enter name2: ")
# lang=input("Enter his fav lang: ")
# d.update({name:lang})
# name=input("Enter name3: ")
# lang=input("Enter his fav lang: ")
# d.update({name:lang})
# name=input("Enter name4: ")
# lang=input("Enter his fav lang: ")
# d.update({name:lang})
# print(d)


# #P7: If the name is same in P6 then what will be result
# #P8: If the langauge is same in P6 then what will be result
# d={}
# name=input("Enter name1: ")
# lang=input("Enter his fav lang: ")
# d.update({name:lang})
# name=input("Enter name2: ")
# lang=input("Enter his fav lang: ")
# d.update({name:lang})
# name=input("Enter name3: ")
# lang=input("Enter his fav lang: ")
# d.update({name:lang})
# name=input("Enter name4: ")
# lang=input("Enter his fav lang: ")
# d.update({name:lang})
# print(d)
'''
Let input be:
Enter name1: Amit
Enter his fav lang: python
Enter name2: Priya
Enter his fav lang: Java
Enter name3: Amit
Enter his fav lang: cpp
Enter name4: Piyush
Enter his fav lang: Java
Output: {'Amit': 'cpp', 'Priya': 'Java', 'Piyush': 'Java'}
Amit's value will be updated with cpp because key must be unique and immutable but the value are mutuable
'''


#P9: Can you chnage the values inside a list which is contained in below set
'''
s={8, 7, 12, "Priya", [1,2]}
'''
'''
Return a TypeError in Python.
Reason:
Lists are mutable (i.e., their values can be changed).
Sets in Python can only contain immutable (hashable) objects. Since lists are mutable, they are not hashable and therefore cannot be added to a set directly.
How to fix it:
If you want to have a collection like [1, 2] inside a set, you should use a tuple (which is immutable) instead of a list:
s = {8, 7, 12, "Priya", (1, 2)}  # Using a tuple instead of a list

- **Sets** are mutable, but the elements inside a set must be **immutable** (i.e., hashable).
- **Tuples** are immutable, meaning you **cannot change their contents** after creation.
- **Lists** are mutable, but since they are **unhashable**, they **cannot** be added to a set.

s = {8, 7, 12, "Priya", (1, 2)}

- `8`, `7`, `12`, and `"Priya"` are immutable (integers and string).
- `(1, 2)` is a **tuple**, which is immutable.

### Can You Change the Tuple `(1, 2)`?
No, you **cannot modify** the contents of `(1, 2)` directly because it's immutable.  
However, you can **remove the old tuple** and **add a new one** if you want to "simulate" a change:

### Example:
s.remove((1, 2))    # Remove the old tuple
s.add((3, 4))       # Add a new tuple
print(s)

**Output:** {8, 7, 12, 'Priya', (3, 4)}

If you were thinking about a **list** instead of a tuple, remember:  
- You **cannot** have a list as an element in a set because lists are unhashable.

'''
