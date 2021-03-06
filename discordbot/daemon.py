#!/usr/bin/python3
# coding: utf-8

import traceback
import discord
from discord.ext import commands
import random
import math
import time
from mutagen.mp3 import MP3
import configparser

def main():

    #configèª­ã¿è¾¼ã¿
    config_ini = configparser.ConfigParser()
    config_ini.read('config.ini', encoding='utf-8')

    token = config_ini['DEFAULT']['TOKEN']
    bot = commands.Bot(command_prefix='!501 ')

    @bot.event
    async def on_ready():
        print('-----Logged in info-----')
        print(bot.user.name)
        print(bot.user.id)
        print(discord.__version__)
        print('------------------------')

    @bot.command()
    async def hello(ctx):
        return await ctx.send('ð©ð©ð©')

    @bot.command()
    async def korosu(ctx):
        return await ctx.send('ãªã¡ã¼ãæ­»ã­')

    @bot.command()
    async def sound(ctx):
        state = ctx.author.voice  # ã³ãã³ãå®è¡èã®VCã¹ãã¼ã¿ã¹ãåå¾
        if state is None:
            return await ctx.send('```\nVCã«åå ãã¦ãã ãã\n```')

        await ctx.author.voice.channel.connect()  # VCã«åå 
        await listen(ctx)
        return await ctx.guild.voice_client.disconnect()  # VCããåæ­

    async def listen(ctx):
        ctx.guild.voice_client.play(discord.FFmpegPCMAudio(config_ini['DEFAULT']['FILEPATH']))
        time.sleep(5)

    @bot.command()
    async def leave(ctx):

        await ctx.guild.voice_client.disconnect()  # VCããåæ­

        return

    @bot.command()
    async def member(ctx):
        state = ctx.author.voice  # ã³ãã³ãå®è¡èã®VCã¹ãã¼ã¿ã¹ãåå¾
        if state is None:
            return await ctx.send('```\nVCã«åå ãã¦ãã ãã\n```')

        name = [member.name for member in ctx.author.voice.channel.members]
        namejoin = '\n'.join(name)

        return await ctx.send('```\n'+namejoin+'\n```')

    @bot.command()
    async def shuffle(ctx):
        state = ctx.author.voice  # ã³ãã³ãå®è¡èã®VCã¹ãã¼ã¿ã¹ãåå¾
        if state is None:
            return await ctx.send('```\nVCã«åå ãã¦ãã ãã\n```')

        list = [member.name for member in ctx.author.voice.channel.members]
        random.shuffle(list)

        teama = []
        teamb = []

        if len(list) <= 1:
            return await ctx.send('```\næä½2äººä»¥ä¸åå ãã¦ãã ãã\n```')

        elif len(list) % 2 == 0:
            memberCountEven = int(len(list) / 2)

            for i in range(memberCountEven):
                teama.append(list[i])

            for i in range(memberCountEven):
                teamb.append(list[memberCountEven+i])

            teamaStr = '\n'.join(teama)
            teambStr = '\n'.join(teamb)

        else:
            memberCountOdd = math.floor(len(list) / 2)

            for i in range(memberCountOdd):
                teama.append(list[i])

            for i in range(memberCountOdd+1):
                teamb.append(list[memberCountOdd+i])

            teamaStr = '\n'.join(teama)
            teambStr = '\n'.join(teamb)

        return await ctx.send('***-----TEAMA-----***\n```md\n'+teamaStr+'```\n' +
                              '\n***-----TEAMB-----***\n```diff\n'+teambStr+'```\n')

    bot.run(token)


if __name__ == "__main__":
    print('start bot')
    main()
