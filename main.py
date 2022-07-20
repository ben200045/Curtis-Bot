import os
import discord
import time

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
    time.sleep(1)
    await message.channel.send('Hahahaha')
    
    await message.add_reaction('👍')

client.run(my_secret)

