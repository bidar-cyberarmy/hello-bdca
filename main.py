import os
import discord
my_secret = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
  print('im here {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello Bina Darma Cyber Army !')

client.run(os.getenv('TOKEN'))