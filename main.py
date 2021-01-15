import time

# Credits: Hello! I do not take any credit to this game under no circumstances. I wanted to make a textbased game and thought that this game would work well! All credit to the game goes to it's original creators who posted it on Unearthed Arcana Reddit. Here is the link to the original manual: https://drive.google.com/file/d/1exUoUk4gNaJa6SB4Fz7STngM8Cu_njdN/view

#Thank you for being here :)

#make a function that adresses what to do if they say something unexpected

#variables
affirmative_answers = ["yes", "yeah", "sure", "yup"]
negative_answers = ["no", "nah", "nope"]
no_count = 0

print("Welcome to Dr. Sunshine's Sublime Circus\n")

answer = input("Would you like this adventure's overview? ")

if answer.lower() in affirmative_answers:
  exit
elif answer.lower() in negative_answers:
  no_count += 1
  answer = input("\naww...that's too bad. Are you sure? ")
  if answer.lower() in affirmative_answers:
    print("\nokie, bye!\n")
    quit()
  else:
    print("\nhaha! we knew you couldn't resist!")
else:
  print("\nummm....that's an answer I do not understand. I am still a robot you know. I'll assume you meant yes :)")
  
print("\n In this text based roleplaying game, you (the player) will have a chance to navigate the world in Dr. Sunshine's Sublime Circus through a series of yes or no answers. \nYou will get the chance to be whisked away to a festive circus nestled in a whimsical, verdant valley. \nAfter discovering a great and dangerous secret about the circus, you must try and escape the piercing gaze of Dr. Sunshine's true, terrifying form. \nWill you be able to get out, or will you become a more permanent fixture of the circus?\n")

time.sleep(5)

answer = input("Now that you know what's going on, let's begin! I will be your guide, your DM I suppose.  Ready to start? ")

if answer in affirmative_answers:
  print("\nPerfect, let's go!")
elif answer in negative_answers:
  if no_count > 0:
    print("\nNow you're just being stubborn! Let's go anyway!")
  no_count += 1
else:
  print("\nummm....that's an answer I do not understand. I am still a robot you know. I'll assume you meant yes :)")

print("\nYou and your group find yourself in a tavern. Though it wouldn't have been renowned for it's interior decorating, it holds an undeniable allure that drew your party to it. \nYou notice the bright colorful posters plastered across the walls of the tavern. All of them identical, featuring a a sharp featured, half-masked man. \nFrom the distance, you can see that the posters say, 'Come one, come all! Got a case of the blues? Visit Dr.Sunshine's Sublime Circus of Wonder and Awe. He'll fix you right up!'")

answer = input("\nWould you like to approach the posters? ")

if answer in affirmative_answers:
 print("\nYour party approaches the posters lining the tavern, intrigued.")
elif answer in negative_answers:
  no_count += 1
  print("\nJust as your party came to the decision that the poster was quite boring and unworthy of your time, a patron of the tavern calls out to you: \n 'oi! You lot 'ave got to visit that there circus! I ain't never 'ad more fun in me life, and I've led quite a life! All you got t'do is touch it.'")
  print("\nRelectunt but intrigued by the patron's recommendation, your party aproaches the posters.")  

print("\nAs one of the players reaches out to touch the garish poster, a flutter of confetti spews from the smiling mouth of the central figure, swirling around you all like a small tornado. An out-of-tune trumpet blares a fanfare, drowning out the noise of surprised tavern goers.\n Suddenly, the confetti fades, and you are standing in a tavern no longer. Rather, the twilight of a distant sun illuminates a verdant valley. The sounds of revelry and festivity hang in the air, their source dominating your view: a collection of brightly colored circus tents. Farther along the path, at the end of the valley, a huge big top looms above all else, dominating your view.")

answer = print("\nWhat would you like to do?")