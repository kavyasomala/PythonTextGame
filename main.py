''''
Credits: Hello! I do not take any credit to this game under no circumstances. I wanted to make a textbased game and thought that this game would work well! 
All credit to the game goes to it's original creators who posted it on Unearthed Arcana Reddit. 
Here is the link to the original manual: 
https://drive.google.com/file/d/1exUoUk4gNaJa6SB4Fz7STngM8Cu_njdN/view

Thank you for being here :)
'''

#make a function that adresses what to do if they say something unexpected
#make a function to adress if the user ever wants to exit the game

import time
import os
import discord 
from discord.ext import commands

#variables
affirmative_answers = ("yes", "yeah", "sure", "yup")
negative_answers = ("no", "nope", "nah", "naw", "not a chance", "sorry")
exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later", "stop")
all_responses = affirmative_answers + negative_answers + exit_commands
no_count = 0

TOKEN = '****************'

client = commands.Bot(command_prefix = '.')

@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. Try .help for a list of possible responses. ({error})')

client.remove_command('help')

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.green())
    embed.set_author(name='Help : list of acceptable answers or topics')
    for i in all_responses:
      embed.add_field(name='.' + i, value='Self Explained', inline=False)
    await ctx.send(embed=embed)

@client.command()
async def start(ctx):
  await ctx.send("Welcome to Dr. Sunshine's Sublime Circus.")
  await ctx.send("Would you like this adventure's overview?")
  def check(msg):
          return msg.author == ctx.author and msg.channel == ctx.channel

  msg = await client.wait_for("message", check=check)
  if msg.content.lower() in affirmative_answers:
    await ctx.send("Yay!")
    print("JUST KIDDING I'M HERE")
  elif msg.content.lower() in negative_answers:
    await ctx.send("Are you sure?")
    msg = await client.wait_for("message", check=check)
    if msg.content.lower() in affirmative_answers:
      await ctx.send("Okie, bye!")
      quit()
    elif msg.content.lower() in negative_answers:
      await ctx.send("Knew you couldn't resist haha")
  else:
    await ctx.send("I don't understand.")


  await ctx.send("In this text based roleplaying game, you (the player) will have a chance to navigate the world in Dr. Sunshine's Sublime Circus through a series of given answers.")
  await ctx.send("You will get the chance to be whisked away to a festive circus nestled in a whimsical, verdant valley.")
  await ctx.send("After discovering a great and dangerous secret about the circus, you must try and escape the piercing gaze of Dr. Sunshine's true, terrifying form.")
  await ctx.send("Will you be able to get out, or will you become a more permanent fixture of the circus?")

'''

  print("\nIn this text based roleplaying game, you (the player) will have a chance to navigate the world in Dr. Sunshine's Sublime Circus through a series of given answers. \nYou will get the chance to be whisked away to a festive circus nestled in a whimsical, verdant valley. \nAfter discovering a great and dangerous secret about the circus, you must try and escape the piercing gaze of Dr. Sunshine's true, terrifying form. \nWill you be able to get out, or will you become a more permanent fixture of the circus?\n")

  time.sleep(5)

  answer = input("Now that you know what's going on, let's begin! I will be your guide, your DM I suppose.  Ready to start? ")
  chat_check(answer)

  if answer:
      print("\nPerfect, let's go!")
  elif not answer:
    if no_count > 0:
      print("\nNow you're just being stubborn! Let's go anyway!")
    no_count += 1

  print("\nYou and your group find yourself in a tavern. Though it wouldn't have been renowned for it's interior decorating, it holds an undeniable allure that drew your party to it. \nYou notice the bright colorful posters plastered across the walls of the tavern. All of them identical, featuring a a sharp featured, half-masked man. \nFrom the distance, you can see that the posters say, 'Come one, come all! Got a case of the blues? Visit Dr.Sunshine's Sublime Circus of Wonder and Awe. He'll fix you right up!'")
  answer = input("\nWhat would you like to do? \n a - approach the posters \n b - order a drink \n c - look around the tavern")

  chat_check(answer)

  if answer:
    print("\nYour party approaches the posters lining the tavern, intrigued.")
  elif not answer:
    no_count += 1
    print("\nJust as your party came to the decision that the poster was quite boring and unworthy of your time, a patron of the tavern calls out to you: \n 'oi! You lot 'ave got to visit that there circus! I ain't never 'ad more fun in me life, and I've led quite a life! All you got t'do is touch it.'")
    print("\nRelectunt but intrigued by the patron's recommendation, your party aproaches the posters.")  

  print("\nAs one of the players reaches out to touch the garish poster, a flutter of confetti spews from the smiling mouth of the central figure, swirling around you all like a small tornado. An out-of-tune trumpet blares a fanfare, drowning out the noise of surprised tavern goers.\n Suddenly, the confetti fades, and you are standing in a tavern no longer. Rather, the twilight of a distant sun illuminates a verdant valley. The sounds of revelry and festivity hang in the air, their source dominating your view: a collection of brightly colored circus tents. Farther along the path, at the end of the valley, a huge big top looms above all else, dominating your view.")
  print("\nWhat would you like to do?")

  end_game()
  quit()
  
def unknown_response():
  print("\nSorry, I didn't understand what you said? Could you please try again?")
  chat()
  
def end_game():
  print("You have reached the end of the game. Thank you for playing!")
 
def exit():
  print("Okay, good bye! It was nice having you, please come back soon.")

#def choices(answer): #eventually change these from multiple choice to NLP so the user has more freedom
'''
client.run(TOKEN)
