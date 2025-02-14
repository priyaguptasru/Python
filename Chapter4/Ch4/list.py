'''List: 
In Python, a list is a built-in dynamic sized array (automatically grows and shrinks). 
We can store all types of items (including another list) in a list. A
list may contain mixed type of items, this is possible because a list mainly stores references at contiguous locations and actual items maybe stored at different locations.
List can contain duplicate items.
List in Python are Mutable. Hence, we can modify, replace or delete the items in the same list.
List are ordered. It maintain the order of elements based on how they are added.
Accessing items in List can be done directly using their position (index), starting from 0.
List can be created as: var_name=[ele1, ele2, ele3, ....so on]
Example:'''
# a=[] #empty list
# print(type(a))
# print(a)
# # print(type(a[0]))
# b=[1]
# print(type(b))
# print(b)
# print(type(b[0]))
# c=['1']
# print(type(c))
# print(c)
# print(type(c[0]))
# d=[1, 9.34, 'c', 'hello', False]
# print(type(d))
# print(d)


'''List Indexing: A list can be index just like a string that is fisrt value is indexed as a index 0 and the second value is indexed as index 1 and the last value is indexed as (lenght-1)
Example:'''
#a=[1, 9.34, 'c', 'hello', False, 6]
# print(a[0]) #Return 1 as value on index 0 is 1
# print(a[4]) #Return False as value on index 4 is False
# print(a[-1]) #Return 6 as value on index -1 is 6 --> a[-1]=a[lenght-1]
# print(a[8]) ##Return error as there is no index 8

# a=[1, 9.34, 'c', 'hello', False, 6]
# print(a) #print the original list
# print(len(a)) #print the length of the list
# print(slice(a[1:4])) #print the list after slicing as per the given
# print(slice(a[1:4:2])) #print the list after slicing as per the given
# print(a) #print the original list


'''Some methods/functions of list in python:'''

# # append(): Adds an element to the end of the list.
# # Syntax: list_name.append(element)
# a = [1, 2, 3]
# print(a)
# a.append(4)
# print(a)


# # copy(): Returns a shallow copy of the list.
# # Syntax: list_name.copy()
# a = [1, 2, 3]
# print(a)
# b = a.copy()
# print(b)


# # clear(): Removes all elements from the list.
# # Syntax: list_name.clear()
# a = [1, 2, 3]
# print(a)
# a.clear()
# print(a)


# # count(): Returns the number of times a specified element appears in the list.
# # Syntax: list_name.count(element)
# a = [1, 2, 3, 1]
# print(a)
# print(a.count(1))
# print(a)


# # extend(): Adds elements from another list to the end of the current list.
# # Syntax: list_name.extend(iterable)
# a = [1, 2]
# print(a)
# a.extend([3, 4, 1, 6, 8])
# print(a)


# # index(): Returns the index of the first occurrence of a specified element.
# # Syntax: list_name.index(element)
# a = [1, 2, 3, 4, 2, 3, 2]
# print(a)
# print(a.index(2)) # Find the index of first occurance of number 2 in the list
# print(a)


# # insert(): Inserts an element at a specified position.
# # Syntax: list_name.insert(index, element)
# a = [1, 3, 4, 5, 6, 7]
# print(a)
# a.insert(1, 2)
# print(a)


# # pop(): Removes and returns the element at the specified position (or the last element if no index is specified).
# # Syntax: list_name.pop(index)
# a = [1, 2, 3, 4, 5, 6]
# print(a)
# a.pop()
# print(a)
# a.pop(2)
# print(a)


# # remove(): Removes the first occurrence of a specified element.
# # Syntax: list_name.remove(element)
# a = [1, 2, 3, 2, 2, 5, 6]
# print(a)
# a.remove(2)
# print(a)


# # reverse(): Reverses the order of the elements in the list.
# # Syntax: list_name.reverse()
# a = [1, 2, 3]
# print(a)
# a.reverse()
# print(a)


# # sort(): Sorts the list in ascending order (by default).
# # Syntax: list_name.sort(key=None, reverse=False)
# a = [3, 1, 2, 1, 2, 6, 9, 2, 0, 3]
# print(a)
# a.sort() # Sort the list in ascending order
# print(a)