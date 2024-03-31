import discord
from discord.ext import commands
from discord import Interaction

import pandas as pd

with open('./key/TOKEN.txt','r') as f:
    TOKEN = f.readline()

client = commands.Bot(command_prefix="!", intents= discord.Intents.all())

@client.event
async def on_ready():
    await client.tree.sync()
    await client.change_presence(activity = discord.activity.Game(name='Working'), # 플레이중인 게임 이름
                                 status = discord.Status.online) # 봇의 상태
    
# ctx.author.id 디스코드 사용자 고유 ID # 숫자로 이뤄져있음
# ctx.author.display_name 프로필 이름
# ctx.author.global_name 사용자 원래이름
# ctx.author.name 사용자명

@client.command(name='asd')
async def init(ctx: commands.context.Context,*arg):
    name = ctx.author.display_name
    id = ctx.author.id
    money = arg.split()[0]
    memo = arg[len(money):].lstrip()
    money = int(money)
    await ctx.send(f'name : {name}, id : {id}\nmoney : {money}, memo : {memo}')

client.run(TOKEN)