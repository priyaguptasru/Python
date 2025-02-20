#P2: 

import random

def game():
    score = random.randint(1, 100) #Take a random number from 1 to 100

    try:
        with open(r'C:\Users\Lenovo\Desktop\pythonCWH\Ch9\practice9\P2.txt', 'r') as f:
            P2 = f.read().strip()  # .strip() Remove extra spaces or newlines
            if P2:  # Check if file is not empty
                P2 = int(P2)  # Convert string to integer
            else:
                P2 = 0  # Default score if file is empty
    except FileNotFoundError:
        P2 = 0  # If file doesn't exist, assume 0

    print(f"Your score is: {score}")

    if score > P2:
        print("New high score!")
        with open(r'C:\Users\Lenovo\Desktop\pythonCWH\Ch9\practice9\P2.txt', 'w') as f:
            f.write(str(score))  # Save new high score

game()
