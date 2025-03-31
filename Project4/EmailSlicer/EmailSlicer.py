'''
Email Slicer is just a simple tool that will take an email address as input and slice it to produce the username and the domain associated with it. The email must be divided into two strings by using ‘@’ as the separator.
For example
Input:
InterviewBit@gmail.com
Output:
Your username is InterviewBit & domain is gmail.com
'''

# Simple code:
# emailaddress=input("Enter the email address: ")
# index=emailaddress.find("@")
# usrnm=emailaddress[:index]
# dom=emailaddress[index+1:]
# print(f"Your username is {usrnm} & domain is {dom}")


# Better code:
from email_validator import validate_email, EmailNotValidError #importing the module which check if user has entered the valid email address or not

while True: #Run the below till the user enter the correct email address
    emailaddress=input("\nEnter the email address: ")

    try: #Run this code if user entered the valid email address
        valid = validate_email(emailaddress)
        index=emailaddress.find("@") #Spilting the email address in two parts by finding @
        usrnm=emailaddress[:index] #taking the first part which is before @
        dom=emailaddress[index+1:] #taking the second part which is after @
        print(f"\nYour username is '{usrnm}' & domain is '{dom}'\n")
        break

    except EmailNotValidError as e: #Print the below line when user has entered the invalid email
        print("\nInvalid email address. Please enter the valid one. \nThank You!\n")

# Note: Install the library from the terminal using the command: pip install email-validator --user