import discord
import random
import asyncio
import pickle
import os
import requests
import json
import time
from nsfc import *
from vk_integ import *
from imgur_integ import *
from wolfram_integ import *
from boto.s3.connection import S3Connection
from funs import *
#from google_integ import *
from accuw_integ import *
from games import *

discord_token=os.environ['DISCORD_TOKEN']

try:
   commands=''
   comand_list = ['\n!help - показать список команд','\n!goals - показать список текущих целей','\n!rasp - расписание пар на завтра','\n!rgoals - добавить цель','\n!r 24  for i in range (len(comand_list)):
   commands = commands+comand_list[i]
                  
client = discord.Client()
@client.event
async def on_ready():
 await client.change_presence(game=discord.Game(name="захват мира"))
 print('Logged on')
 print(client.user.name)
 print(client.user.id)
 print("-------------")
 logging.info("Bot started")
                  
@client.event
async def on_message(message):
 if message.content.startswith('!ping'):
    await client.send_message(message.channel, 'pong')

 elif message.content.startswith('!help'):
     await  client.send_message(message.channel,'```Спискок команд:' + commands + ' ```')
 
 elif message.content.startswith('!isalexcool'):
            await client.send_message(message.channel,'Of course!')
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
            if message.content[6:]=='btc':
               curs=Curs_BTC()
            else:
               curs=Curs()
         await client.send_message(message.channel, curs)

 elif message.content.startswith('!test'):
        await client.send_message(message.channel,':sunny:')
client.run(discord_token)
except Exception:
  print('Fatal error!')
