import random
computer = random.choice(['Stone', 'Paper', 'Scissors'])
user=input("Enter your choice(Stone/Paper/PaperScissors): ")
print(f"Computer's choice is: {computer}\nYour's choice is: {user}")

if(computer == user):print("It's a Tie!!!")
else:
    if(computer=='Stone' and user=='Paper'):print("You Win!!!")
    elif(computer=='Stone' and user=='Scissors'):print("You Loss!!!")
    elif(computer=='Paper' and user=='Stone'):print("You Loss!!!")
    elif(computer=='Paper' and user=='Scissors'):print("You Win!!!")
    elif(computer=='Scissors' and user=='Stone'):print("You Win!!!")
    elif(computer=='Scissors' and user=='Paper'):print("You Loss!!!")
    else:print("Something wemt wrong...")

