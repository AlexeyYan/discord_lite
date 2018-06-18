import discord
import asyncio
import pickle
import os
from requests import *
import json
from datetime import datetime
client = discord.Client()
@client.event
async def on_ready():
 print('Logged on')
 print(client.user.name)
 print(client.user.id)
 print("-------------")

@client.event
async def on_message(message):
  time=str(datetime.now())
  
  if message.content.startswith('!help'):
         await  client.send_message(message.channel,'```Спискок команд:\n!help - показать список команд\n!goals - показать список текущих целей\n!rasp - расписание пар на завтра\n!rgoals - добавить цель```')

  elif message.content.startswith('!isalexcool'):
         await client.send_message(message.channel,'Of course!')

  elif message.content.startswith('!rasp'):
         r=requests.get('https://students.bsuir.by/api/v1/studentGroup/schedule?studentGroup=740401')
         week=requests.get('http://students.bsuir.by/api/v1/week').json()
         leng=len(r.json()['tomorrowSchedules'])
         i=0
         if r.json()['tomorrowSchedules']!=[]:
            while i<leng:
                 if week in r.json()['tomorrowSchedules'][i]['weekNumber'] or r.json()['tomorrowSchedules']!=None:
                  time=('Время: ' + r.json()['tomorrowSchedules'][i]['lessonTime'])
                  sub=('Предмет: ' + r.json()['tomorrowSchedules'][i]['subject']+' ('+r.json()['tomorrowSchedules'][i]['lessonType']+')')
                  aud=('Аудитория: ' + r.json()['tomorrowSchedules'][i]['auditory'][0])
                  await client.send_message(message.channel,time + '\n' + sub + '\n' + aud +'\n'+'----------------\n')
                  i+=1
                 else: await client.send_message(message.channel,'Завтра пар нет, гуляем)')
  client.run('NDI1Njk5NDM5NTk3MDYwMDk2.DZVeoA.ErWcwG-mu7w6a9IfaJCPUOSyOwo')

