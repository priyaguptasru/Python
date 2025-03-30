'''
Program to calculate your age in which it take your date of birth and then return your age after caluting it from the current date.
# '''

from datetime import datetime #For getting today's date
from dateutil.relativedelta import relativedelta #To calculate the exact difference between today and the date of birth.

dob_str = input("Enter your date of birth (yyyy-mm-dd) : ") #User's input in the string type
dob = datetime.strptime(dob_str, "%Y-%m-%d") #Converting it in the date format

today = datetime.today() #Get today's date

difference = relativedelta(today, dob) #Calculate the difference using relativedelta

print(f"You are {difference.years} years, {difference.months} months, and {difference.days} days old.")

#Note: Install the library from the terminal using the command: pip install python-dateutil --user