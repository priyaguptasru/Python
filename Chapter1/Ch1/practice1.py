# #P1: Write a program to print "Twinkle Twinkle" poem in python
# print('''
# Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the trav'ller in the dark,
# Thanks you for your tiny spark,
# He could not see which way to go,
# If you did not twinkle so.

# In the dark blue sky you keep,
# And often thro' my curtains peep,
# For you never shut your eye,
# Till the sun is in the sky.

# 'Tis your bright and tiny spark,
# Lights the trav'ller in the dark:
# Tho' I know not what you are,
# Twinkle, twinkle, little star.
# ''')


# # P2: Use REPL and print the table of 5
# '''Enter in REPL and print the table by entering the number one by one
# >>> 5*1
# 5
# >>> 5*2
# 10
# >>> 5*3
# 15
# >>> 5*4
# 20
# and so on
# OR
# Enter in REPL and use loops
# >>> for i in range(1, 11):print(5, '*', i, '=', 5*i)
# ...
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
# 5 * 10 = 50'''


# #P3: Install an external module and use it to perform an operation of your interest.
# '''here we use 'python text-to-speech' module
# install the above module through terminal using below cmd
# cmd: pip install pyttsx3 or pip install pyttsx3 --user
# now import it in our code'''
# import pyttsx3
# speak = pyttsx3.init()
# speak.say("Hey! This code is written by Priya Gupta.")
# speak.runAndWait()


# #P4: Write a python program to print the contents of a directory using the os module
# import os

# # Specify the directory you want to list
# directory_path_of_C = '/' #This will list the files of C drive
# directory_path_of_pythonCWH = '/Users/Lenovo/Desktop/pythonCWH'  #This will list the files of mentioned folder

# # Get the list of files and directories in the specified directory

# print('Files in C drive are: ')
# contents = os.listdir(directory_path_of_C )
# # Print the contents
# for item1 in contents:
#     print(item1)

# print('------')

# print('Files in pythonCWH folder are: ')
# contents = os.listdir(directory_path_of_pythonCWH )
# # Print the contents
# for item2 in contents:
#     print(item2)
