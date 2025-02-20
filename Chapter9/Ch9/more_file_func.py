f=open(r'C:\Users\Lenovo\Desktop\pythonCWH\Ch9\more_file_func.txt' , 'r')

# read and print the whole content at once
# lines=f.readlines()
# print(lines, type(lines))
# f.close()

# read and print the line one by one
# line1=f.readline()
# print(line1, type(line1))
# line2=f.readline()
# print(line2, type(line2))
# line3=f.readline()
# print(line3, type(line3))
# line4=f.readline()
# print(line4, type(line4))
# line5=f.readline() #return blank as there is no line 5 in the file.
# print(line5, type(line5))
# f.close()

# OR

# read and print the lines one by one
# line=f.readline()
# while(line != ""):
#     print(line, type(line))
#     line=f.readline()
# f.close()