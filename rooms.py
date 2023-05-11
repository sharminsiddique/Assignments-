# Go to Hell Game

from random import choice

def room1():
    # Dragon room
    print ("\nYou are in the room with three dragons which are "
           "fire dragon, acid dragon and ice dragon. If you pick "
           "one of these dragons. It will let you excape this room to "
           "their homeland.")
    
    dragon = input("\nWhich dragon do you prefer? "
               "\n(fire / acid / ice): ")

    if dragon.lower() == "fire":
        print("\nYou choose the fire dragon and it try to blow fire on you "
              "so you run to the acid dragon to save yourself and able to "
              "climb on it. You make acid dragon uncomfortable and it "
              "start to fly.")

    elif dragon.lower() == "ice":
        print("\nYou choose the ice dragon and it try to kill you so "
              "you run to the acid dragon to save yourself and able to climb "
              "on it. You make acid dragon uncomfortable and it start to fly.")

    elif dragon.lower() == "acid":
        print("\nYou choose acid dragon and able to climb on it. You make "
              "acid dragon uncomfortable and it start to fly.")


def room2():
    # Chemical room
    print ("\nAcid dragon bring you to the acid land and you had to enter "
           "Chemical Room because of other dragons around you. \nIn this room, "
           "you saw three diffrent chemical pool. "
           "\n\nThere is a warning and it says: "
           "\n\tThis is our warning to the traveler who comes to this room, "
           "\n\tYou can jump into one of the chemical pools, "
           "\n\tAt the bottom of each pool, you will find the secret passage, "
           "\n\tBut if you swim in the chemical, you get a mysterious animal trait.")

    color = input("\nNow write the color of the most innocent colorful pool."
           "\n(Green/Red/Blue): ")

    if color.lower() == "green":
        print("\nThis pool has turned you into a cat-human. "
              "Now you have cat agility, but just like a cat, "
              "your whole body is covered with cat hair. "
              "Luckily you made it through the portal and found yourself "
              "in the Brains' Chamber.")
        ability = "cat"
        
    if color.lower() == "red":
        print("\nThis pool has turned you into a flea-human. "
              "Now you can jump 200 times your height like a flea, "
              "but now you're a dwarf. Luckily you made it through the portal "
              "and found yourself in the Brains' Chamber.")
        ability = "flea"
        
    if color.lower() == "blue":
        print("\nThis pool has turned you into a chameleon-human. "
              "Now, even though your skin looks like the skin of a chameleon, "
              "you have the ability to camouflage a chameleon. "
              "Luckily you made it through the portal and found yourself "
              "in the Brains' Chamber.")
        ability = "chameleon"


def room3():
    # Brains' Chamber
    print ("\nYou saw a letter next to the brains. It says you should eat "
           "one of these brains and this will let you pass to the other room. "
           "CHOOSE WISELY!")
    brain = input("\nWhich brain do you prefer? (Human/Pig/Bat): ")

    if brain.lower() == "human":
        print(f"\nYou lost the skill you gained in the chemical pool "
              "and you are all human again.")
    if brain.lower() == "pig":
        print("\nPigtail has now been added to the skill you gained "
              "in the chemical pool.")
    if brain.lower() == "bat":
        print("\nThe bat tooth has now been added to the skill "
              "you gained in the chemical pool.")
    print("\nYour head started spinning and you passed out.")

def room4():
    # Room of darkness
    print("When you open your eyes, you find yourself in a labyrinth. "
          "\n\nThere are three doors in front of you. "
          "\n - The door on the left leads to a raging inferno."
          "\n - The door in the center leads to a deadly assassin."
          "\n - The door on the right leads to a lion that hasn't eaten "
          "in three months.")
    door = input("\nWhich door do you choose? (left/center/right): ")

    book_of_deeds = ["sin", "virtue"]
    deeds = choice(book_of_deeds)

    options = ["lost", "win"]
    result = choice(options)

    if door.lower() == "left":
        
       if deeds == "virtue":
            print("\nWhen you stepped into inferno, you chose to die and your "
                  "book of deeds was opened. It was decided that your virtues "
                  "were greater than your sins and you were carried to heaven "
                  "by angels. Now you will live your eternal life in heaven.")
       if deeds == "sin":
           print("\nWhen you stepped into inferno, your book of deeds was opened. "
                 "It was decided that your sins were greater than your virtues. "
                 "You will now live your eternal life in inferno.")
 
    if door.lower() == "center":
        print(f"\nWhen you entered the room of the deadly assassin, he suddenly "
              "attacked you. You started fighting him with the skill you've "
              f"gained before and you {result.upper()}.")
        if result == "lost":
            print("\nYou DIED.")
            if deeds == "virtue":
                print("\nIt was decided that your virtues were greater than your "
                      "sins and you were carried to heaven by angels. "
                      "Now you will live your eternal life in heaven.")
            if deeds == "sin":
                print("\nIt was decided that your sins were greater than your virtues. "
                      "You will now live your eternal life in inferno.")
        if result == "win":
            print ("\nYou managed to escape from all the rooms. "
                   "Now you can go back to your life and start living "
                   "knowing the value of your life.")
            
        
    if door.lower() == "right":
        print(f"\nWhen you entered the hungry lion's room, it suddenly attacked you. "
              "You started fighting the lion with the skill you've gained before "
              f"and you {result.upper()}.")
        if result == "lost":
            print("\nYou DIED.")
            if deeds == "virtue":
                print("\nIt was decided that your virtues were greater than your "
                      "sins and you were carried to heaven by angels. "
                      "Now you will live your eternal life in heaven.")
            if deeds == "sin":
                print("\nIt was decided that your sins were greater than your virtues. "
                      "You will now live your eternal life in inferno.")
        if result == "win":
            print ("\nYou managed to escape from all the rooms. "
                   "Now you can go back to your life and start living "
                   "knowing the value of your life.")


welcome = "Hello Adventurer. Do you wanna play this 'Go to Hell Game'? "
welcome += "\nWhen you feel ready to start, type 'START' and the game will begin: "

welcome = input (welcome)

if welcome.lower() == "start":
    room1()
    room2()
    room3()
    room4()

