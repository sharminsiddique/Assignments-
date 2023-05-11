import random
unk_num = random.randint(0,100)

game = '''Welcome to guess the number. 
You need to guess a number,
between 0-100.
Have fun guessing! '''

print(game)

user = int(input("Please guess a number between 0 and 100!"))

while True:
    if user == unk_num:
        break
    if user != unk_num:
        if user > unk_num:
            print("Your guess is too high")
        elif user < unk_num:
            print ("Your guess is too low")     
    user = int(input("Guess again:"))
    

    


