'''Tuples:
Python Tuple is a collection of objects separated by commas. A tuple is similar to a Python list in terms of indexing, nested objects, and repetition but the main difference between both is Python tuple is immutable, unlike the Python list which is mutable.
Like Lists, tuples are ordered and we can access their elements using their index values
We cannot update items to a tuple once it is created. 
Tuples cannot be appended or extended.
We cannot remove items from a tuple once it is created.
Note : In case of list, we use square brackets []. BUt in tuple, we use round brackets ()
Example:
'''
# t1 = (10, 20, 30) #Tuple
# print(t1) #Return (10, 20, 30)
# print(type(t1)) #Type is Tuple
# t2 = () #Empty Tuple
# print(t2) #Return ()
# print(type(t2)) #Type is Tuple
# t3 = (1) #Here, python will treat it as a integer value
# print(t3) #Return 1
# print(type(t3)) #Here, python will treat it as a integer value therefore return it as a interger type
# t4 = (1,) #Here, python will treat it as a Tuple because ',' is  mentioned
# print(t4) #Retrurn (1,)
# print(type(t4)) #Type is Tuple

# t1 = (1, 2, 3, 4, 5)
# print(t1[1]) # tuples are indexed
# print(t1[4])

# t2 = (1, 2, 3, 4, 2, 3) # tuples contain duplicate elements
# print(t2)

# t3 = (1, 2, 3, 4, 5)
# t3[1] = 100 # updating an element
# print(t3) #Return error as Tuple is immutable.


'''Methods/Function of Tuple in Python: Python Tuples is an immutable collection of that are more like lists. Python Provides a couple of methods to work with tuples.'''

# # Count() Method: Returns the number of times the given element appears in the tuple.
# # Syntax: tuple_name.count(element)
# Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2) 
# Tuple2 = ('python', 'geek', 'python', 'for', 'java', 'python', 'python') 
# res = Tuple1.count(3) # count the appearance of 3 
# print('Count of 3 in Tuple1 is:', res) 
# res = Tuple2.count('python') # count the appearance of python 
# print('Count of Python in Tuple2 is:', res)

# # Counting tuples and lists as elements in Tuples
# Tuple = (0, 1, (2, 3), (2, 3), 1, [3, 2], 'geeks', (0,)) 
# res = Tuple.count((2, 3)) # count the appearance of (2, 3) 
# print('Count of (2, 3) in Tuple is:', res) 
# res = Tuple.count([3, 2]) # count the appearance of [3, 2] 
# print('Count of [3, 2] in Tuple is:', res)


# Index() Method: Returns the first occurrence of the given element from the tuple.
# Syntax: tuple_name.index(element, start, end) 
'''NOTES:
element: The element to be searched.
start (Optional): The starting index from where the searching is started
end (Optional): The ending index till where the searching is done
Note: This method raises a ValueError if the element is not found in the tuple.
Example:'''
# Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2) 

# res = Tuple.index(3) # getting the index of 3 
# print('First occurrence of number 3 is at index', res) 

# res = Tuple.index(3, 4) # getting the index of 3 after 4th index 
# print('First occurrence of number 3 after 4th index is:', res)

# res = Tuple.index(4) # getting the index of 3 
# print('First occurrence of 4 is', res) #Return error as elememt is not found in the memtioned tuple
