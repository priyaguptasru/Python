#Write a program to generate a random number and ask the user to guess it correct. Also print the score.(score=100-number_of_attempt_taken)


from random import randint
rn=randint(1,10)
# print(rn)
count=0
guess=int(input("Enter your guessed number: "))

while(guess != rn):
    count +=1
    if(guess > rn):print("\nWrong!!!\nYour guessed number is greater than the actual number. Please enter any smaller number.\n")
    else:print("\nWrong!!!\nYour guessed number is smaller than the actual number. Please enter any greater number.\n")
    guess=int(input("Enter your guessed number: "))
score=100-count
print(f"\nCongratulations!!! You have guessed the correct number.\nYour score is {score}\n")