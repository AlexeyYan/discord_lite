import discord
import asyncio
import pickle
import os
import requests
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
  if message.content.startswith('!goals'):
   try:
      f=open('discordbot/goals.txt','r')
      mp=f.read();
      f.close
      await client.send_message(message.channel,mp)
   except:
      f=open('discordbot/logs.txt','a')
      f.write(time+' Ошибка работы с командой !goals')
      f.close

  elif message.content.startswith('!help'):
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
  elif message.content.startswith('!rgoals'):
       goals_list=[]
       username = message.author.name
       f=open('discordbot/goals.txt','a')
       goals_list.append(message.content[8:])
       print('Пользователь ' + username + ' добавил цель:\n- ' + goals_list[0] + ' -')
       f.write('- '+goals_list[0]+'\n-----------------------\n')
       f.close
       if message.server.name== 'Lamp Night':
        main=message.server.get_channel('425280734614519830')
       elif message.server.name== 'Bots':
        main=message.server.get_channel('434344740096442368')
       #print(main.get_channel('434344740096442368'))
       await client.send_message(message.channel, 'OK')
       await client.send_message(main,'Добавлена цель:\n' + goals_list[0],tts=True)

client.run('NDI1Njk5NDM5NTk3MDYwMDk2.DZVeoA.ErWcwG-mu7w6a9IfaJCPUOSyOwo')

