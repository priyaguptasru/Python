'''Set:
A Set in Python is used to store a collection of items with the following properties.
No duplicate elements. If try to insert the same item again, it overwrites previous one.
An unordered collection. When we access all items, they are accessed without any specific order and we cannot access items using indexes as we do in lists.
Internally use hashing that makes set efficient for search, insert and delete operations. It gives a major advantage over a list for problems with these operations.
Mutable, meaning we can add or remove elements after their creation, the individual elements within the set cannot be changed directly.
Python sets can store heterogeneous elements in it, i.e., a set can store a mixture of string, integer, boolean, etc datatypes.
'''
# s1=[]
# print(s1, type(s1))
# s2=() #It si empty tuple
# print(s2, type(s2))
# s3={} #It is empty dictionary
# print(s3, type(s3))
# s4=set() #It is empty set
# print(s4, type(s4))

# s={1,2,2,6,4,9,3}
# print(s, type(s))

# # typecasting list to set
# # my_set=set()
# s = set(["a", "b", "c", 7, False, 2.9, 7, 'a'])
# print(s)

# adding element to the set
# s = set(["a", "b", "c", 7, False, 2.9, 7, 'a'])
# s.add("d")
# print(s)

# # a set cannot have duplicate values
# s = {"Geeks", "for", "Geeks"}
# print(s)

# # values of a set cannot be changed
# s = {"Geeks", "for", "Geeks"}
# s[1] = "Hello"
# print(s)


'''Python Frozen Sets:
Frozen sets in Python are immutable objects that only support methods and operators that produce a result without affecting the frozen set or sets to which they are applied. It can be done with frozenset() method in Python.
While elements of a set can be modified at any time, elements of the frozen set remain the same after creation. 
If no parameters are passed, it returns an empty frozenset.
Example:'''
# # Python program to demonstrate differences between normal and frozen set
# s = set(["a", "b","c"]) #Normal Set
# print("Normal Set: ",s)
# fs = frozenset(["e", "f", "g"]) #Frozen Set
# print("\nFrozen Set: ",fs)
# # Uncommenting below line would cause error as we are trying to add element to a frozen set
# # fs.add("h")


# Common Set Methods:

# # add(element):Adds a single element to the set. If the element is already present, it won’t be added again (because sets contain only unique elements).
#    s = {1, 2, 3}
#    s.add(4)  # s becomes {1, 2, 3, 4}

# # remove(element):Removes the specified element from the set. If the element is not found, it raises a KeyError.
#    s = {1, 2, 3}
#    s.remove(2)  # s becomes {1, 3}

# # discard(element):Removes the specified element from the set if it exists. Unlike `remove()`, it does not raise an error if the element is not found.
#    s = {1, 2, 3}
#    s.discard(4)  # s remains {1, 2, 3} (no error)

# # pop():Removes and returns an arbitrary element from the set. Since sets are unordered, which element gets removed is not guaranteed.
#    s = {1, 2, 3}
#    popped = s.pop()  # popped will be one of the elements, e.g., 1, and the set will be updated

# # clear():Removes all elements from the set, leaving it empty.
#    s = {1, 2, 3}
#    s.clear()  # s becomes set()

# # copy():Returns a shallow copy of the set (a new set with the same elements).
#    s = {1, 2, 3}
#    s_copy = s.copy()  # s_copy is a new set {1, 2, 3}


# Set Operations (Methods for Set Algebra):

# # union(other_set) or `|` : Returns a new set containing all elements from both sets.
#    s1 = {1, 2, 3}
#    s2 = {3, 4, 5}
#    s3 = s1.union(s2)  # s3 = {1, 2, 3, 4, 5}

# # intersection(other_set) or `&` : Returns a new set with elements common to both sets.
#    s1 = {1, 2, 3}
#    s2 = {3, 4, 5}
#    s3 = s1.intersection(s2)  # s3 = {3}

# # difference(other_set) or `-` : Returns a new set with elements in the set but not in the other set.
#    s1 = {1, 2, 3}
#    s2 = {3, 4, 5}
#    s3 = s1.difference(s2)  # s3 = {1, 2}

# # symmetric_difference(other_set) or `^` : Returns a new set with elements that are in either set but not in both.
#     s1 = {1, 2, 3}
#     s2 = {3, 4, 5}
#     s3 = s1.symmetric_difference(s2)  # s3 = {1, 2, 4, 5}
 

# Set Information Methods:

# # issubset(other_set): Returns `True` if the set is a subset of the other set (i.e., all elements of the set are in the other set).
#     s1 = {1, 2}
#     s2 = {1, 2, 3}
#     print(s1.issubset(s2))  # True

# # issuperset(other_set): Returns `True` if the set is a superset of the other set (i.e., the set contains all elements of the other set).
#     s1 = {1, 2, 3}
#     s2 = {1, 2}
#     print(s1.issuperset(s2))  # True

# # isdisjoint(other_set): Returns `True` if the two sets have no elements in common.
#     s1 = {1, 2, 3}
#     s2 = {4, 5, 6}
#     print(s1.isdisjoint(s2))  # True

# # len(): Returns the number of elements in the set.
#     s = {1, 2, 3}
#     print(len(s))  # 3

# # in: Checks if an element is in the set.
#     s = {1, 2, 3}
#     print(2 in s)  # True
#     print(4 in s)  # False

