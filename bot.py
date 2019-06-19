import discord
import random
import asyncio
import pickle
import os
import requests
import json
import time
from datetime import datetime
import helps
from vk_integ import Vk_Integration
from imgur_integ import *
from funs import *
from yandex_integ import Yandex
from random_integ import Rand
from bsuir_integ import Get_Schedules

discord_token = os.environ['DISCORD_TOKEN']
client = discord.Client()
vk = Vk_Integration()
yandex=Yandex()
Rand=Rand()
GAMES = ['Skynet', 'программирование', 'кубики',
         '*не играет*', 'CS:GO', 'рок группе', 'песочнице', 'пьесе']


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name=random.choice(GAMES), status=discord.Status.idle))
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
            answer = Get_Schedules(1)
        else:
            answer = Get_Schedules(0)
        await client.send_message(message.channel, answer)

    elif message.content.startswith('!randvk'):
        mem = vk.random_pic()
        await client.send_message(message.channel, mem)

    elif message.content.startswith('!randpic'):
        pic = Random_Pic()
        await client.send_message(message.channel, pic)

    elif message.content.startswith('!dice'):
        cube1, cube2 = Rand.Dice()
        name = message.author.name
        await client.send_message(message.channel, name+': выпало '+cube1+' и '+cube2)

    elif message.content.startswith('!flip'):
        ans=Rand.Flip()
        await client.send_message(message.channel, 'Выпало: '+ans)

    elif message.content.startswith('!roll'):
        amount=1
        name = message.author.name
        dip = str(message.content[6:]).split(' ')
        if dip:
            if int(dip[2])!=0:
                amount=int(dip[2])
        ans = Rand.Roll(int(dip[0]), int(dip[1]), amount)
        await client.send_message(message.channel,  name+f', ваши числа: {ans}')

    elif message.content.startswith('!weather'):
        forecast=yandex.GetWeather()
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.blue(), title='***Погода***', description=ans))

    elif message.content.startswith('!curs'):
        if message.content[6:] == 'all':
            curs = Curs_All()
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), title='***Основные курсы валют на сегодня:***', description=curs))
        else:
            curs = Curs()
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), title='***Курсы валют на сегодня:***', description=curs))

    elif message.content.startswith('!qr'):
        value = message.content[4:]
        createQRCode(value)
        qr = open('qr.jpg', 'rb')
        await client.send_file(message.author, qr)
        await client.delete_message(message)

    elif message.content.startswith('!help'):
        if message.content[6:] != '':
            if message.content[6:] in helps.Commands_richList.keys():
                answer = discord.Embed(color=discord.Color.blue(
                ), title='__***'+message.content[6:]+' - help***__', description=helps.Commands_richList[message.content[6:]])
            else:
                answer = discord.Embed(color=discord.Color.red(
                ), title='__***Error!***__', description='Команда не найдена')
        else:
            answer = discord.Embed(color=discord.Color.blue(
            ), title='__***Commands List***__', description=helps.Commands_List)
        await client. send_message(message.author, embed=answer)
        await client.delete_message(message)

    elif message.content.startswith('!pz'):
        story = vk.pozor_story()
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), title='___***Позор***___', description=story))

    elif message.content.startswith('!test'):
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.blue(), description='''```diff\n- Here's some red colored text!\n```'''))

    elif message.content.startswith('!stat'):
        await client.change_presence(game=discord.Game(name=random.choice(GAMES), type=0))


@client.event
async def on_message_delete(message):
    print('User {} delete message: {}'.format(
        message.author.name, message.content))


@client.event
async def on_member_join(member):
    await client.send_message(member, 'Приветсвую {} на нашем сервере {}!'.format(member.name, member.guild.name))
    await client.send_message(os.environ['MAIN'], '{} вступил в нашу команду, поделитесь печеньками)'.format(member.name))

client.run(discord_token)
