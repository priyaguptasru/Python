# #P1: Write a program to find the greatest of four number entered by the user
# n1=int(input("Enter number 1: "))
# n2=int(input("Enter number 2: "))
# n3=int(input("Enter number 3: "))
# n4=int(input("Enter number 4: "))
# if(n1>=n2 and n1>=n3 and n1>=n4):print(n1, " is greatest")
# elif(n2>=n1 and n2>=n3 and n2>=n4):print(n2, " is greatest")
# elif(n3>=n1 and n3>=n2 and n3>=n4):print(n3, " is greatest")
# else :print(n4, " is greatest")


# #P2: Write a program to check if the student is pass or fail; if it requires overall 40% and 33% in each subjects. Assume 3 subjects and take marks as an input from the user.
# Eng=int(input("Enter marks of english: "))
# Hin=int(input("Enter marks of hindi: "))
# Math=int(input("Enter marks of maths: "))
# total_per=(((Eng+Hin+Math)/300)*100)
# if((Eng>=33 and Hin>=33 and Math>=33) and total_per>=40):print(f"Total percentage: {total_per} \nPASS!!!")
# else :print(f"Total percentage: {total_per} \nFAIL!!!")


# #P3:A spam comment is defined as a text containing following keywords: "make a lot of money", "buy now", "subscribe this", "buy this". Write a program to detect this spam
# spam_keys=["make a lot of money", "buy now", "subscribe this", "buy this"]
# text=input("Enter your comment: ")
# if any(keyword in text.casefold() for keyword in spam_keys):print("Alert!!! This is spam.") #using for-in loop for searching the span_keys in the text. casefold() is used for ignoring the3 case sensitivity.The any() function is a built-in Python function that returns True if at least one element of an iterable is truthy. If all elements are falsy, it returns False.
# else: print("Thanks for your comment.")


# #P4: Write a program to find if the given username contain less than 10 characters or not
# username=input("Enter the username: ")
# len_of_un=len(username)
# if(len_of_un <= 10):print(f"{len_of_un} : Username contain less than or equal to 10 characters")
# else : print(f"{len_of_un} : Username contain more than 10 characters")


# #P5: Write a program to find out if the given name is present in the list or not
# name_list=["Priya", "Piyush", "Amit", "Madhuri", "Ajay", "Soumya", "Sneha"]
# name=input("Enter the name: ")
# if (name.casefold() in [nl.casefold() for nl in name_list]):print("Name is present.")
# else:print("Name is not present.")


# #P6: Write a program to calculate the grade of the student from his marks following the below scheme
# '''
# 90-100 -->Ex
# 80-89 -->A
# 70-79 -->B
# 60-69 -->C
# 50-59 -->D
# <50 -->E
# '''
# marks=int(input("Enter marks of the student: "))
# if(marks<=100 and marks>=90):print("Grade: EX")
# elif(marks<90 and marks>80):print("Grade: A")
# elif(marks<80 and marks>=70):print("Grade: B")
# elif(marks<70 and marks>=60):print("Grade: C")
# elif(marks<60 and marks>=50):print("Grade: D")
# else:print("Grade: E")


#P7: Write a program to check if the given post is talking about "Python" or not
# post=input("Enter the post: ")
# if("python" in post.casefold()):print("YES! The post is about python.")
# else:print("NO! The post is not about python.")