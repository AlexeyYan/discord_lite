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
client.run('NDI2MDE1MzAxOTUyMzM5OTY4.DZQBlg.bCwyfXTtRmoHlvw6w8W2xo9OooY')
