#!/usr/bin/python3

import traceback
import discord
from discord.ext import commands
import random
import math


def main():

    token = 'tokenhere'
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
        return await ctx.send('💩💩💩')

    @bot.command()
    async def korosu(ctx):
        return await ctx.send('オメーが死ね')

    @bot.command()
    async def member(ctx):
        state = ctx.author.voice  # コマンド実行者のVCステータスを取得
        if state is None:
            return await ctx.send('```\nVCに参加してください\n```')

        name = [member.name for member in ctx.author.voice.channel.members]
        namejoin = '\n'.join(name)

        return await ctx.send('```\n'+namejoin+'\n```')

    @bot.command()
    async def shuffle(ctx):
        state = ctx.author.voice  # コマンド実行者のVCステータスを取得
        if state is None:
            return await ctx.send('```\nVCに参加してください\n```')

        list = [member.name for member in ctx.author.voice.channel.members]
        random.shuffle(list)

        teama = []
        teamb = []

        if len(list) <= 1:
            return await ctx.send('```\n最低2人以上参加してください\n```')

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