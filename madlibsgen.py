# Take information from user and fit it into story

name = input("What is your name? ")
city = input("Which city do you want to be? ")
animal = input("Which animal do you like the most? ")
place = input ("Where do you want to be? ")
activity = input("What do you do in your dreams? ")
mood = input ("What is your mood? ")
with_who = input ("Who do you want to be with? ")
punish = input ("What do you want to do to punish them? ")

story = f"\nI'am {name.title()}. "
story += f"I'am living in {city.title()} with {with_who.title()}. "
story += f"I feel {mood}. \nI lost my {animal} when I was {activity}."
story += f"\nI called {with_who} and they said they had eaten {animal}. "
story += f"\nI decided to {punish} them and then they died. \nTHE END"

print (story)


