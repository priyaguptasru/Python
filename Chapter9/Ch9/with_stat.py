'''
Using with Statement
with statement is used for resource management. It ensures that file is properly closed after its suite finishes, even if an exception is raised. with open() as method automatically handles closing the file once the block of code is exited, even if an error occurs. This reduces the risk of file corruption and resource leakage.
'''
# with open(r"C:\Users\Lenovo\Desktop\pythonCWH\Ch9\with_stat.txt") as file:
#     content = file.read()
#     print(content)


'''
Handling Exceptions When Closing a File
It’s important to handle exceptions to ensure that files are closed properly, even if an error occurs during file operations.
'''
# try:
#     file = open(r"C:\Users\Lenovo\Desktop\pythonCWH\Ch9\with_stat.txt")
#     content = file.read()
#     print(content)
# finally:
#     file.close()
