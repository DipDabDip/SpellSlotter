import discord
import os

client = discord.Client()

class player():
  def __init__(self):
    self.name = 'Unnamed Player'
    self.spells = []
  
  def givespells(n):
    for x in range(n):
      player.spells[n] = 0

def listToString(s):  
    str1 = ""  
    
    for ele in s:  
        str1 += ele   
    
    return str1  

def getword(s):
  count = 0
  wordend = False
  length = len(s)
  word = ''
  while wordend and count < length:
    if s[count] != " ":
      word += s[count]
    else:
      wordend = True
    count += 1
  return word
      

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Ollie likes'):
        await message.channel.send('Penis!')

    if message.content.startswith('s/addplayer'):
        msg = list(message.content)
        del msg[:12]
        msg = listToString(msg)
        print(getword(msg))
        await message.channel.send(msg)


client.run(os.getenv('TOKEN'))
