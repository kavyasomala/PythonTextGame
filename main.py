''''
Credits: Hello! I do not take any credit to this game under no circumstances. I wanted to make a textbased game and thought that this game would work well! 
All credit to the game goes to it's original creators who posted it on Unearthed Arcana Reddit. 
Here is the link to the original manual: 
https://drive.google.com/file/d/1exUoUk4gNaJa6SB4Fz7STngM8Cu_njdN/view

Thank you for being here :)
'''

#BUGS TO FIX:
#make a function that adresses what to do if they say something unexpected
#make a function to adress if the user ever wants to exit the game
#remove choices and make it into nlp instead
#start bot when user comes online instead of waiting for them to type start
#help command doesn't always work

import time
import os
import discord 
from discord.ext import commands

#variables
affirmative_answers = ("yes", "yeah", "sure", "yup", "okay", "of course", "alright", "certainly", "absolutely", "by all means", "yup", "ok", "okie", "yea")
negative_answers = ("no", "nope", "nah", "naw", "not a chance", "sorry", "never", "no way")
exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later", "stop")
all_responses = affirmative_answers + negative_answers + exit_commands
no_count = 0

TOKEN = "***************************************"

client = commands.Bot(command_prefix = '.')

client.remove_command('help')

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.green())
    embed.set_author(name='Help : list of acceptable answers or topics')
    embed.add_field(name = ".help", value='Brings up menu of possible responses and topics available.', inline=False)
    embed.add_field(name = ".start", value='Begins the adventure.', inline=False)
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
  elif msg.content.lower() in negative_answers or msg.content.lower() in exit_commands:
    await ctx.send("Are you sure?")
    msg = await client.wait_for("message", check=check)
    if msg.content.lower() in affirmative_answers or msg.content.lower() in exit_commands:
      await ctx.send("Okie, bye!")
      exit()
    elif msg.content.lower() in negative_answers:
      await ctx.send("Knew you couldn't resist haha")
    else:
      await ctx.send("Error. I do not understand that command. Try .help for a current list of possible responses.")
      exit()
  else:
    await ctx.send("Error. I do not understand that command. Try .help for a current list of possible responses.")
    exit()

  await ctx.send("In this text based roleplaying game, you (the player) will have a chance to navigate the world in Dr. Sunshine's Sublime Circus through a series of given answers.")
  await ctx.send("You will get the chance to be whisked away to a festive circus nestled in a whimsical, verdant valley.")
  await ctx.send("After discovering a great and dangerous secret about the circus, you must try and escape the piercing gaze of Dr. Sunshine's true, terrifying form.")
  await ctx.send("Will you be able to get out, or will you become a more permanent fixture of the circus?")
  await ctx.send("Now that you know what's going on, let's begin!")
  await ctx.send("If you would like to exit at any point, just say any exit command.")
  await ctx.send("Ready to start?")

  msg = await client.wait_for("message", check=check)
  if msg.content.lower() in affirmative_answers:
    await ctx.send("Perfect, let's go!")
    await ctx.send("Here is the map for this adventure:")
    await ctx.send("https://preview.redd.it/gx79c9oqey561.png?width=1700&format=png&auto=webp&s=c2a5b629dfd346bad797a764946ed91bb4323952")
  elif msg.content.lower() in negative_answers or msg.content.lower() in exit_commands:
    await ctx.send("Aww. Sorry to see you go I guess. Bye! Come back soon!")
    exit()
  else:
    await ctx.send("Error. I do not understand that command. Try .help for a current list of possible responses.")
    exit()
  
  await ctx.send("You and your group find yourself in a tavern.")
  await ctx.send("Though it wouldn't have been renowned for it's interior decorating, it holds an undeniable allure that drew your party to it.")
  await ctx.send("You notice the bright colorful posters plastered across the walls of the tavern. All of them identical, featuring a a sharp featured, half-masked man.")
  await ctx.send("From the distance, you can see that the posters say, 'Come one, come all! Got a case of the blues? Visit Dr.Sunshine's Sublime Circus of Wonder and Awe. He'll fix you right up!'")
  
  await ctx.send("What would you like to do?")
  await ctx.send("a - approach the posters \nb - find a table \nc - order a drink\nd - leave")
  
  msg = await client.wait_for("message", check=check)
  print(msg.content.lower())  
  if msg.content.lower() == 'a':
    await ctx.send("Your party approaches the posters lining the tavern, intrigued.")
  if msg.content.lower() == 'b':
    await ctx.send("You find a table easily enough. The tavern is fairly empty, consisting only of a few patrons and the bartender wiping down the surfaces.")
    await ctx.send("As you settle down, you hear a patron calling out to you: 'oi! You lot 'ave got to visit that there circus! I ain't never 'ad more fun in me life, and I've led quite a life! All you got t'do is touch it.'")
    await ctx.send("Intrigued, a member of your party approaches the posters on the nearest wall. The rest of your party slowly follows.")
  if msg.content.lower() == 'c':
    await ctx.send("You approach the bartender, hoping to order a drink and perhaps some food. As you walk over, you hear a patron calling out to you: 'oi! You lot 'ave got to visit that there circus! I ain't never 'ad more fun in me life, and I've led quite a life! All you got t'do is touch it.")
    await ctx.send("Now curious of the the posters because of the patron's recommendation, your party aproaches the posters.")  
  if msg.content.lower() == 'd':
    await ctx.send("Your party came to the conclusion that the allure you all felt to the tavern was for naught for the tavern was actually quite boring and unworthy of your time.")
    await ctx.send("Just as you turn to leave, a patron calls out to you: 'oi! You lot 'ave got to visit that there circus! I ain't never 'ad more fun in me life, and I've led quite a life! All you got t'do is touch it.'")
    await ctx.send("Relectunt but curious neverthless by the patron's recommendation, your party aproaches the posters.")  
  
  await ctx.send("Cautiously, a member of your party reaches out to touch the garish poster.")
  await ctx.send("As soon as their hand comes into contact, a flutter of confetti spews from the smiling mouth of the central figure, swirling around you all like a small tornado.")
  await ctx.send("An out-of-tune trumpet blares a fanfare, drowning out the noise of surprised tavern goers.")
  await ctx.send("Suddenly, the confetti fades, and you are standing in a tavern no longer. Rather, the twilight of a distant sun illuminates a verdant valley.")
  await ctx.send("The sounds of revelry and festivity hang in the air, their source dominating your view: a collection of brightly colored circus tents. Farther along the path, at the end of the valley, a huge big top looms above all else, dominating your view.")
  await ctx.send("What would you like to do?")
  
client.run(TOKEN)

'''
Story to make into code:
1. Gate of the Sun
  Players are whisked away from the tavern to the midst of this
  massive arch, located opposite the big top at the other end of
  the valley. Players who inspect the stone arch notice crude
  carvings of the sun covering its surface, but they see no
  obvious means to return.
  Once players get their bearings, they hear the following:
    A voice barks from the nearby tent: "Well, are you just gonna
    stand there, or are you ready for some fun!"
  The voice comes from the visitor's center (area 2).
2. Visitor's Center
  Inside this tent stands a festive illusion (see Appendix A)
  behind a wooden counter. The thin, smiling apparition of a
  female elf seems real, even to the touch. Players would need
  to succeed on a DC 30 Wisdom (Insight or Perception) check
  in order to notice the minor inconsistencies present in the
  illusion.
  This illusion, like all other circus patrons, is controlled by
  Dr. Sunshine, and acts like an over-excited, overly-interested
  employee. It answers any questions players have about the
  activities at the circus, giving exuberant, energetic replies.
  No matter what else is said, the apparition emphasizes the
  following:
    "Oh, and you absolutely must see the doctor! His grand show
    never fails to amaze, and I've never seen anyone leave it
    without a smile on their face. Seriously! It's over at the big top,
    you can't miss it."
  Treasure. Players can grab a free souvenir from the gift
  shop, either a hat with a spinning sunburst on top or a carved,
  painted sunburst necklace.
3. Mirror Maze
A hunched barker stands outside this square building's single
entrance, his voice rising as players approach:
  "Step right up, try and navigate the maze of mirrors! Whoever
  can manage it wins a wondrous prize!"
The barker is in reality one of the lost* in disguise, its urges
kept in check (for now) by Dr. Sunshine. The incredibly
convincing illusion can only be seen through with a
successful DC 30 Wisdom (Insight or Perception) check. The
same goes for all other disguised sorrowsworn.
Though the barker makes it seem like a challenge, the
mirror maze is quite easy, and players can make it through
with a successful DC 18 Intelligence (Investigation) or
Wisdom (Insight) check. On a failure, the player leading the
group walks into a mirror.
Treasure. On a success, players navigate the maze and
emerge on the other side, where the barker stands, ready
with their prize:
  Mirror of Farsight (requires attunement)
    This gilded mirror worked in the shape of a sunburst glows
    ever so slightly in sunlight.
    As an action, the wielder can view any place they have seen
    within 10 miles, as if using the scrying spell.
    Curse. Once the true nature of the circus is revealed (see
    Part 2), this mirror's curse manifests, unbeknownst to the
    wielder. Afterward, there is a cumulative 20 percent chance
    that when used, the mirror shows not the desired location,
    but instead a small, dark room. In the corner stands an
    unnaturally tall, skinny figure, facing away from the wielder --
    an odraz (see Appendix A). If the wielder continues to gaze
    upon the odraz, it emerges through the mirror and attacks.
  
    If players try to scry on Dr. Sunshine, either
    through the mirror or their own magic, before
    meeting him, they see him in his dressing room.
    Turning to look directly at the viewer, Dr.
    Sunshine reveals his maskless face, which
    resembles stretched black leather. Through an
    unnaturally large smile, Dr. Sunshine gives a wink
    and a wave, whispering "shh, don't spoil the
    surprise..." The scrying then fails, along with any
    future attempt.
  
4. Ettin Beheadin'