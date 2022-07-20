import os
import discord
import time
import random

my_secret = os.environ['TOKEN']
client = discord.Client()

@client.event
async def on_ready():
  print('Curtis Bot. Online. Analyzing Curtis.')
  print(client.user)

@client.event
async def on_message(message):
  #Admiration Module
  if message.author.name == 'Pesto': #Change to 'Pesto'
    if(random.randint(1,5) > 2):       #60% chance of activation
      sleepTimer = random.randint(2,20)
      await message_roulette(message, sleepTimer)
      await reaction_roulette(message, sleepTimer)

async def message_roulette(message, sleepTimer):
  if(sleepTimer == 2):
    await message.channel.send('woah, mama mia cunt')
    return

async def reaction_roulette(message, sleepTimer):
  #await message.add_reaction('👍')
  time.sleep(sleepTimer) #Response time between 2-20 seconds
  for reacts in range(1,4): #Runs 4 times
    time.sleep(0.8)
    await add_react(message)

async def add_react(message):
  reactions = random.randint(1,20)
  if(reactions == 1):
    await message.add_reaction('👍') # 5% chance
  if(reactions == 2):
    await message.add_reaction('😂') # 5% chance
  if(reactions == 3):
    await message.add_reaction('😳') # 5% chance
  if(reactions == 4):
    await message.add_reaction('😆') # 5% chance
  if(reactions == 5):
    await message.add_reaction('😒') # 5% chance  
  if(reactions == 6):
    await message.add_reaction('🤪') # 5% chance
  if(reactions == 7):
    await message.add_reaction('👏') # 5% chance
  else:
    return                           # 65% chance

client.run(my_secret)

