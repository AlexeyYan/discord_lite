import discord
import asyncio
client = discord.Client()
@client.event
async def on_ready():
 print('Logged on')
 print(client.user.name)
 print(client.user.id)
 print("-------------")

@client.event
async def on_message(message):  
  if message.content.startswith('!isalexcool'):
         await client.send_message(message.channel,'Of course!')
  client.run('NDI1Njk5NDM5NTk3MDYwMDk2.DZVeoA.ErWcwG-mu7w6a9IfaJCPUOSyOwo')

