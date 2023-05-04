message1 = input("Would you like to roll the dice? yes or no?")
print(message1)
answer1 = "yes"
answer2 = "no"
while message1 == answer2:
    print("Ok, thank you for your time. See you again, goodbye")
    break
if message1 == answer1:
    import random
    print(random.randrange(1, 7))
message2 = input("Would you like to roll again? yes or no?")
print(message2)
answer3 = input("yes")
answer4 = input("no")