import random
import asyncio
import pickle
import os
import requests
import json
import time
import subprocess
from datetime import datetime

import discord
from youtube_dl import YoutubeDL

import helps
from vk_integ import Vk_Integration
from funs import *
from yandex_integ import Yandex
from random_integ import Rand
from bsuir_integ import Get_Schedules


class ProBot(discord.Client):

    async def on_ready(self):
        self.vk = Vk_Integration()
        self.yandex = Yandex()
        self.rand = Rand()
        self.ydl = YoutubeDL({'forcejson': True, 'simulate': True, 'quiet':True})
        self.games = ['Skynet', 'программирование', 'кубики',
                      '*не играет*', 'рок группе', 'песочнице', 'пьесе', 'админа']
        self.players = {}
        print(f'Logged on\n{self.user.name}\n{self.user.id}\n{"-"*13}')
        await self.change_presence(activity=discord.Game(name=random.choice(self.games),
                                                         status=discord.Status.idle))

    async def on_message(self, message):
        if message.content.startswith('!ping'):
            await message.channel.send('pong')

        elif message.content.startswith('!rasp'):
            if message.content.startswith('!rasp next'):
                answer = Get_Schedules(1)
            else:
                answer = Get_Schedules(0)
            await message.channel.send(answer)

        elif message.content.startswith('!randvk'):
            mem = self.vk.random_pic()
            await message.channel.send(mem)

        elif message.content.startswith('!dice'):
            cube1, cube2 = self.rand.Dice()
            name = message.author.name
            await message.channel.send(name+f': выпало {cube1} и {cube2}')

        elif message.content.startswith('!flip'):
            ans = self.rand.Flip()
            await message.channel.send(f'Выпало: {ans}')

        elif message.content.startswith('!roll'):
            amount = 1
            name = message.author.name
            dip = str(message.content[6:]).split(' ')
            if dip:
                if int(dip[2]) != 0:
                    amount = int(dip[2])
            ans = self.rand.Roll(int(dip[0]), int(dip[1]), amount)
            await message.channel.send(f'{name} , ваши числа: {ans}')

        elif message.content.startswith('!weather'):
            forecast = self.yandex.GetWeather()
            await message.channel.send(embed=discord.Embed(color=discord.Color.blue(),
                                                           title='***Погода***',
                                                           description=forecast))

        elif message.content.startswith('!curs'):
            if message.content[6:] == 'all':
                curs = Curs_All()
                await message.channel.send(embed=discord.Embed(color=discord.Color.green(),
                                                               title='***Основные курсы валют на сегодня:***',
                                                               description=curs))
            else:
                curs = Curs()
                await message.channel.send(embed=discord.Embed(color=discord.Color.green(),
                                                               title='***Курсы валют на сегодня:***',
                                                               description=curs))

        elif message.content.startswith('!qr'):
            value = message.content[4:]
            createQRCode(value)
            qr = open('qr.jpg', 'rb')
            await self.send_file(message.author, qr)
            await self.delete_message(message)

        elif message.content.startswith('!help'):
            if message.content[6:] != '':
                if message.content[6:] in helps.Commands_richList.keys():
                    answer = discord.Embed(color=discord.Color.blue(), 
                                           title=f'__***{message.content[6:]} - help***__', 
                                           description=helps.Commands_richList[message.content[6:]])
                else:
                    answer = discord.Embed(color=discord.Color.red(), 
                                           title='__***Error!***__', 
                                           description='Команда не найдена')
            else:
                answer = discord.Embed(color=discord.Color.blue(), 
                                       title='__***Commands List***__', 
                                       description=helps.Commands_List)
            await message.author.send(embed=answer)
            await self.delete_message(message)

        elif message.content.startswith('!pz'):
            story = self.vk.pozor_story()
            await message.channel.send(embed=discord.Embed(color=discord.Color.green(),
                                                                           title='___***Позор***___',
                                                                           description=story))

        elif message.content.startswith('!test'):
            await message.channel.send(embed=discord.Embed(color=discord.Color.blue(), 
                                                                           description='''```diff\n- Here's some red colored text!\n```'''))
        elif message.content.startswith('!setcolor'):
            rgb_color = message.content[10:].split()
            guild = message.channel.guild
            for role in guild.roles:
                if role.name == message.author.display_name:
                    color = discord.Colour.from_rgb(int(rgb_color[0]),
                                                    int(rgb_color[1]),
                                                    int(rgb_color[2]))
                    await role.edit(colour=color)
                    await message.delete()

        # Voice functions
        elif message.content.startswith('!voice'):
            if message.author.voice:
                channel = message.author.voice.channel
                self.voice_client = await channel.connect()

        elif message.content.startswith('!play'):
            url = message.content[7:]
            guild = message.guild
            info = self.ydl.extract_info(url)
            for vformat in info['formats']:
                if vformat['format_id'] == '251':
                    url = vformat['url']
            self.voice_client.play(discord.FFmpegPCMAudio(url))
            self.voice_client.is_playing()

        elif message.content.startswith('!leave'):
            self.voice_client.stop()
            if self.voice_client:
                await self.voice_client.disconnect()

        elif message.content.startswith('!pause'):
            self.voice_client.pause()

        elif message.content.startswith('!resume'):
            self.voice_client.resume()

        elif message.content.startswith('!stop'):
            self.voice_client.stop()

        # Some utils (not works)
        elif message.content.startswith('!del'):
            if message.author.id == 377142726962970634:
                try:
                    amount = message.content[5:]
                    deleted = await message.channel.purge(limit=int(amount)+1)
                except discord.ClientException:
                    await message.channel.send('Максимальное количество удаляемых сообщений 100')

        elif message.content.startswith('!stat'):
            await self.change_presence(game=discord.Game(name=random.choice(self.games), type=0))

    async def on_message_delete(self, message):
        print('User {} delete message: {}'.format(message.author.name, message.content))


if __name__ == "__main__":
    discord_token = os.environ['DISCORD_TOKEN']
    bot = ProBot()
    bot.run(discord_token)
