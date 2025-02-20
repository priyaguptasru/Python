'''
File Handling: File handling refers to the process of performing operations on a file such as creating, opening, reading, writing and closing it, through a programming interface. It involves managing the data flow between the program and the file system on the storage device, ensuring that data is handled safely and efficiently.

Advantages of File Handling in Python
Versatility : Allows us to perform a wide range of operations, such as creating, reading, writing, appending, renaming and deleting files.
Flexibility : Allows us to work with different file types (e.g. text files, binary files, CSV files , etc.) and to perform different operations on files (e.g. read, write, append, etc.).
User-friendly : Python provides a user-friendly interface for file handling, making it easy to create, read and manipulate files.
Cross-platform : Work across different platforms (e.g. Windows, Mac, Linux), allowing for seamless integration and compatibility.

Disadvantages of File Handling in Python
Error-prone: Can be prone to errors, especially if the code is not carefully written or if there are issues with the file system (e.g. file permissions, file locks, etc.).
Security risks : Can also pose security risks, especially if the program accepts user input that can be used to access or modify sensitive files on the system.
Complexity : Can be complex, especially when working with more advanced file formats or operations. Careful attention must be paid to the code to ensure that files are handled properly and securely.
Performance : Can be slower than other programming languages, especially when dealing with large files or performing complex operations.
'''


'''
Opening a File in Python:
To open a file we can use open() function, which requires file path and mode as arguments:
'''
# file = open(r'C:\Users\Lenovo\Desktop\pythonCWH\Ch9\fh.txt')


'''Closing a File
Closing a file is essential to ensure that all resources used by the file are properly released. file.close() method closes the file and ensures that any changes made to the file are saved.
'''
# file = open("fh.txt", "r")
# file.close()


'''
File Modes in Python:
When opening a file, we must specify the mode we want to which specifies what we want to do with the file. Here’s a table of the different modes available:
'''

# r: Read-only mode:- Opens the file for reading. File must exist; otherwise, it raises an error.

# # When file named as fread.txt is present(Run the file)
# f = open(r"C:\Users\Lenovo\Desktop\pythonCWH\Ch9\fread.txt", "r")
# content = f.read()
# print(content)
# f.close()
# # When file named as fread1.txt is not present(Throw the error)
# file=open(r"C:\Users\Lenovo\Desktop\pythonCWH\Ch9\fread1.txt", "r")
# data=file.read()
# print(data)
# file.close()

# rb: Read-only in binary mode:- Opens the file for reading binary data. File must exist; otherwise, it raises an error.

# r+: Read and write mode:- Opens the file for both reading and writing. File must exist; otherwise, it raises an error.

# rb+: Read and write in binary mode:- Opens the file for both reading and writing binary data. File must exist; otherwise, it raises an error.

# -------------------------------------------------------------

# w: Write mode:- Opens the file for writing. Creates a new file or truncates the existing file.

# # When file named as fwrite.txt is present. It replace the original content of the file with the given data.
# data = "I am Priya Gupta. And this is write module."
# file=open(r"C:\Users\Lenovo\Desktop\pythonCWH\Ch9\fwrite.txt", "w")
# file.write(data)
# file.close()
# # When file named as fwrite1.txt is not present. It create the one and write the content in that file.
# data="I am Amit Verma. And I am learning write module."
# file=open(r"C:\Users\Lenovo\Desktop\pythonCWH\Ch9\fwrite1.txt", "w")
# file.write(data)
# file.close()

# wb: Write in binary mode:- Opens the file for writing binary data. Creates a new file or truncates the existing file.

# w+: Write and read mode:- Opens the file for both writing and reading. Creates a new file or truncates the existing file.

# wb+: Write and read in binary mode:- Opens the file for both writing and reading binary data. Creates a new file or truncates the existing file.

# -------------------------------------------------------------

# a: Append mode:- Opens the file for appending data. Creates a new file if it doesn’t exist.

# # When file named as fappend.txt is present. It concatenate the given data in the original data.
# data="\nHello World!!!. I am Priya"
# f=open(r"C:\Users\Lenovo\Desktop\pythonCWH\Ch9\fappend.txt", "a")
# f.write(data)
# f.close()
# # When file named as fappend1.txt is not present. It create the one and concatenate data.
# data="Hello World!!!. This is append module."
# f=open(r"C:\Users\Lenovo\Desktop\pythonCWH\Ch9\fappend1.txt", "a")
# f.write(data)
# f.close()

# ab: Append in binary mode:-	Opens the file for appending binary data. Creates a new file if it doesn’t exist.

# a+: Append and read mode:- Opens the file for appending and reading. Creates a new file if it doesn’t exist.

# ab+: Append and read in binary mode:- Opens the file for appending and reading binary data. Creates a new file if it doesn’t exist.

# -------------------------------------------------------------

# x: Exclusive creation mode:- Creates a new file. Raises an error if the file already exists.

# # When file named as fexclusive is not present. It create a new one and write the content in that file.
# data="This is exclusive module."
# f = open(r"C:\Users\Lenovo\Desktop\pythonCWH\Ch9\fexclusive.txt", "x")
# f.write(data)
# f.close()
# # When file named as fexclusive1 is present. It give an error.
# data="Hi All !!! This is exclusive module."
# f = open(r"C:\Users\Lenovo\Desktop\pythonCWH\Ch9\fexclusive1.txt", "x")
# f.write(data)
# f.close()

# xb: Exclusive creation in binary mode:-	Creates a new binary file. Raises an error if the file already exists.

# x+: Exclusive creation with read and write mode:- Creates a new file for reading and writing. Raises an error if the file exists.

# xb+: Exclusive creation with read and write in binary mode:- Creates a new binary file for reading and writing. Raises an error if the file exists.



