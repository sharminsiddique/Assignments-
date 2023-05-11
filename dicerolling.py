import random

def simulator ():
    dice_rolling = random.randint(1,6)
    print (dice_rolling) 

user_1 = input("Would you like to roll the dice? (yes/no):")

while True:
    if user_1.lower() == "yes":  
        simulator ()
    elif user_1.lower() == "no":
        print ("ok see you again later")
        break
    else:
        print("please answer yes or no")
    user_1 = input("Would you like to roll the dice again (yes/no)?")
    
