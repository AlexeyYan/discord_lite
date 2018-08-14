import discord
import random
import asyncio
import pickle
import os
import requests
import json
import time
from vk_integ import *
from imgur_integ import *
from wolfram_integ import *
from funs import *
from accuw_integ import *
from games import *
from schedules import *
from datetime import datetime

discord_token=os.environ['DISCORD_TOKEN']
            
client = discord.Client()
@client.event
async def on_ready():
 await client.change_presence(game=discord.Game(name="захват мира"))
 print('Logged on')
 print(client.user.name)
 print(client.user.id)
 print("-------------")
                  
@client.event
async def on_message(message):
 if message.content.startswith('!ping'):
    await client.send_message(message.channel, 'pong')
 
 elif message.content.startswith('!rasp'):
      if message.content.startswith('!rasp next'):
         answer=getTomorrowSchedules()
      else:
         answer=getTodaySchedules()
      await client.send_message(message.channel, answer)


 elif message.content.startswith('!randvk'):
        if message.content.startswith('!randvk bntu'):
         mem=Random_BNTU_Mem()
        else:
          if message.content.startswith('!randvk it'):
           mem=Random_IT_Mem()
          else:
           mem=Random_VkMem()
        await client.send_message(message.channel,mem)

 elif message.content.startswith('!randpic'):
      pic = Random_Pic()
      await client.send_message(message.channel,pic)

 elif message.content.startswith('!joke'):
         joke = Random_Joke()
         await client.send_message(message.channel,joke)

 elif message.content.startswith('!wolf'):
         question=str(message.content[6:])
         answer = Question(question)
         await client.send_message(message.channel,answer)

 elif message.content.startswith('!dice'):
         cube1, cube2 = Dice()
         name=message.author.name
         await client.send_message(message.channel, name+': выпало '+cube1+' и '+cube2)

 elif message.content.startswith('!flip'):
         if random.randint(0,1000)<=453 : ans = 'Орёл'
         else: ans = 'Решка'
         await client.send_message(message.channel,'Выпало: '+ans)

 elif message.content.startswith('!weather'):
         result=Daily_Forecast()
         await client.send_message(message.channel,result)

 elif message.content.startswith('!curs'):
        if message.content[6:]=='all':
            curs=Curs_All()
        else:
            curs=Curs()
        await client.send_message(message.channel, curs)
 
 elif message.content.startswith('!inst'):
         url = message.content[6:]
         answer = getInstagramContent(url)
         await client.send_message(message.channel, answer)

 elif message.content.startswith('!test'):
        await client.send_message(message.channel,':sunny:')

async def Kostil():
        await client.wait_until_ready()
        today = datetime.today()
        if today.month not in [6,7,8] and today.weekday() < 7 :
                if (today.hour+3) == 6 and today.minute <= 30:
                        requests.get('https://alexyan9.pythonanywhere.com/api/v1.0/rasp', params = {'start':'1'})
        await asyncio.sleep(1800)
client.loop.create_task(Kostil())
client.run(discord_token)
