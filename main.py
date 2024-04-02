import discord
from discord.ext import commands
from discord import Interaction

import pandas as pd
from datetime import datetime
from deposit import deposit

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
   
@client.command(name='지갑생성')
async def create_wallet(ctx: commands.context.Context) -> None:
    dep, st_id, name = ctx.author.display_name.split()
    dic_id = ctx.author.id
    time = datetime.now()
    try:
        df = pd.read_csv(f'./People_data/{name}_{dic_id}.csv', encoding='utf-8 sig')
        await ctx.send('이미 지갑이 있습니다.')
    except:
        data = {'Name': [name], # str
                'Department': [dep], # str
                'Student_id': [st_id], # str
                'Discord_id': [ctx.author.id], # str
                'Add_credit': [0], # int
                'Total_credit': [0], # int
                'Memo': ['create wallet'], # str
                'Year': [time.year], # str
                'Month': [time.month], # str
                'Day': [time.day]} # str
        df = pd.DataFrame(data)
        df.to_csv(f'./People_data/{name}_{dic_id}.csv', encoding='utf-8-sig')
        await ctx.send('지갑이 생성되었습니다.')

@client.command(name='예금')
async def create_wallet(ctx: commands.context.Context, *, message: str) -> None:  
    # message type : name credit memo
    name, credit = message.split()[0], message.split()[1]
    memo = message[len(name) + len(credit) + 2:]
    credit = int(credit)
    deposit(ctx.author, credit, memo)
    await ctx.send(f'{credit}G 추가했습니다.')

client.run(TOKEN)