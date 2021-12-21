import random

def rolldice(min, max):
    while True:
        print("Rolling dice...")
        number = random.randint(min, max)
        print(f"Your number : {number}")
        choice = input("Do You Want to Roll the Dice Again? (y/n")
        if choice.lower() == 'n':
           break
    


rolldice(1, 6)