'''Dictionary in python:
A Python dictionary is a data structure that stores the value in {key: value} pairs. Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t be repeated and must be immutable.
In Python, a dictionary can be created by placing a sequence of elements within curly {} braces, separated by a ‘comma’.
From Python 3.7 Version onward, Python dictionary are Ordered.
Dictionary keys are case sensitive: the same name but different cases of Key will be treated distinctly.
Dictionary is mutuable.
Keys must be immutable: This means keys can be strings, numbers, or tuples but not lists.
Keys must be unique: Duplicate keys are not allowed and any duplicate key will overwrite the previous value.
Dictionary internally uses Hashing. Hence, operations like search, insert, delete can be performed in Constant Time.
Example:
'''
# d={} #Empty dictionary
# print(d, type(d)) #Print the original dictionary and its type as dict

# age={
#     "Priya": 26,
#     "Amit": 32,
#     "Piyush": 23,
#      27: "Soumya"
# }
# print(age, type(age)) #Print the original dictionary and its type as dict
# print(age['Priya']) #Return the value against key Priya ie 26
# print(age['Harry']) #Return error there is no such key available in the above code


#Some of the funtions/methods of the python dictionary
# # Creating a dictionary
my_dic = {
    "Name": "Priya",
    26: "Age",
    "Country": "India",
    "Ph_no": 745,
    "list_hobby": ['Reading', 'Playing', 'Singing']
}
# print(my_dic) #Return the original dictionary
# print(type(my_dic)) #Return its type ie dict

# # get():Returns the value for the given key
# print(my_dic.get(26)) #Return Age
# print(my_dic.get("Name")) #Return Priya
# print(my_dic["Ph_no"])
# print(my_dic.get("Ph_no"))
# '''Both of these lines will retrieve the value associated with the key "Ph_no" in the dictionary my_dic, but there's a subtle difference in how they handle situations where the key might not exist:
# print(my_dic["Ph_no"])
# This will raise a KeyError if "Ph_no" is not a key in my_dic. It's a direct lookup, so if the key is missing, Python will throw an error.
# print(my_dic.get("Ph_no"))
# This is a safer way to access the value for the key "Ph_no". If the key exists, it will return the value, but if the key is not found, it will return None (or another value you specify as the second argument, like my_dic.get("Ph_no", "Not Found")).
# If "Ph_no" is not in the dictionary, using .get() prevents your program from crashing, whereas using square brackets ([]) will cause an error.'''

# # items():Return the list with all dictionary keys with values
# print(my_dic.items()) #Return the original dictionary
# # print(my_dic.items("Name")) #Return error
# print(list(my_dic.items())[0][1]) #Return Priya
# print(list(my_dic.items())[3][0]) #Return Ph_no

# keys():Returns a view object that displays a list of all the keys in the dictionary in order of insertion. 
# print(my_dic.keys()) #dict_keys(['Name', 26, 'Country', 'Ph_no', 'list_hobby'])
# print(list(my_dic.keys())) #['Name', 26, 'Country', 'Ph_no', 'list_hobby']

# values():Returns a view object containing all dictionary values, which can be accessed and iterated through efficiently.
# print(my_dic.values()) #dict_values(['Priya', 'Age', 'India', 745, ['Reading', 'Playing', 'Singing']])
# print(list(my_dic.values())) #['Priya', 'Age', 'India', 745, ['Reading', 'Playing', 'Singing']]

# update():Updates the dictionary with the elements from another dictionary or an iterable of key-value pairs. With this method, you can include new data or merge it with existing dictionary entries.
# print(my_dic) #Print the original dict
# my_dic.update({"Ph_no": 7030})
# my_dic.update({"Name": "Amit"})
# my_dic.update({"Friend": "Piyush"}) #Add a new key named a Friend as this key is not available earlier
# print(my_dic) #Print after updating the original dict

# clear():Removes all items from the dictionary
# print(my_dic) #Print the original dict
# my_dic.clear()
# print(my_dic) #Return {} after clearing the dict

# copy():Returns a shallow copy of the dictionary
# print(my_dic) #Print the orginal dict
# copy_of_my_dic =my_dic 
# print(copy_of_my_dic)
# '''This line doesn't actually create a new copy of the dictionary; it just creates a reference to the same dictionary. Any change made to copy_of_my_dic will also affect my_dic because both variables point to the same object.'''
# copy_of_my_dic = my_dic.copy()
# print(copy_of_my_dic) 
# '''This line creates a shallow copy of my_dic. It means copy_of_my_dic is a new dictionary that has the same keys and values as my_dic, but changes made to copy_of_my_dic won't affect my_dic unless the dictionary values themselves are mutable (like lists or other dictionaries).'''

# # fromkeys():Creates a dictionary from the given sequence
# print(my_dic) #{'Name': 'Priya', 26: 'Age', 'Country': 'India', 'Ph_no': 745, 'list_hobby': ['Reading', 'Playing', 'Singing']}
# print(my_dic.fromkeys(my_dic, 1)) #{'Name': 1, 26: 1, 'Country': 1, 'Ph_no': 1, 'list_hobby': 1}
# print(my_dic.fromkeys("Ph_no", 1)) #{'P': 1, 'h': 1, '_': 1, 'n': 1, 'o': 1}
# print(my_dic) #{'Name': 'Priya', 26: 'Age', 'Country': 'India', 'Ph_no': 745, 'list_hobby': ['Reading', 'Playing', 'Singing']}        

# pop():Returns and removes the element with the given key
# print(my_dic) #Print original dict
# print(my_dic.pop("Ph_no")) #Return 745 as value against Ph_no
# print(my_dic) #Print the dict after poping out Ph_no--> {'Name': 'Priya', 26: 'Age', 'Country': 'India', 'list_hobby': ['Reading', 'Playing', 'Singing']}
# print(my_dic.pop("Friend")) #Return error as Friend key is not available in the given dict
# print(my_dic)

# popitem():Returns and removes the item that was last inserted into the dictionary.
# print(my_dic) #Print original dict
# print(my_dic.popitem()) #Print the last item of the dict. Here, ('list_hobby', ['Reading', 'Playing', 'Singing'])
# print(my_dic) #Print after performing the above operation. Here, {'Name': 'Priya', 26: 'Age', 'Country': 'India', 'Ph_no': 745}

# # setdefault():Returns the value of a key if the key is in the dictionary else inserts the key with a value to the dictionary
# print(my_dic) #Print the original dict
# print(my_dic.setdefault('Ph_no',7030)) #Return the value of the existing key, but will not modify the dictionary key.
# print(my_dic.setdefault('Friend','Piyush')) #Set a new value it the dict
# print(my_dic) #Print after performing the above operation

