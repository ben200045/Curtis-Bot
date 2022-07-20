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
  if message.author == client.user:
    return
  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')
  
  #Admiration Module
  if message.author.name == 'Jean Pierre Dogé': #Change to 'Pesto'
    if(random.randint(1,5) > 2):       #60% chance of activation
      time.sleep(random.randint(2,20)) #Response time between 2-20 seconds
      message_roulette(message)
      await reaction_roulette(message)

async def message_roulette(message):
  await message.channel.send('Hahahaha')

async def reaction_roulette(message):
  #await message.add_reaction('👍')
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
    await message.add_reaction('😅') # 5% chance
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

