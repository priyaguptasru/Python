#P1: Write a program to read the text from the given file 'P1.txt' and find out if it contains the word ;'twinkle'.

f=open(r'C:\Users\Lenovo\Desktop\pythonCWH\Ch9\practice9\P1.txt')
file = f.read().lower() #.lower() ensures that both uppercase and lowercase versions of "Twinkle" (eg, twinkle, TWINKLE, TwInKlE) are detected.
if('twinkle' in file):print("Yes, word Twinkle is present.")
else:print("No, word Twinkle is not present")
f.close()