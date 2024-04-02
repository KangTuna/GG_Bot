import pandas as pd
from datetime import datetime
import discord
from discord.ext import commands

def deposit(author: commands.context.Context.author, credit: int, memo: str) -> None:
    dep, st_id, name = author.display_name.split()
    dic_id = author.id
    time = datetime.now()
    df = pd.read_csv(f'./People_data/{name}_{dic_id}.csv', encoding='utf-8-sig', index_col=0)
    pre_credit = df['Total_credit'][len(df) -1]
    data = {'Name': [name],
            'Department': [dep],
            'Student_id': [st_id],
            'Discord_id': [dic_id],
            'Add_credit': [credit],
            'Total_credit': [pre_credit+credit],
            'Memo': [memo],
            'Year': [time.year],
            'Month': [time.month],
            'Day': [time.day]}
    
    ddf = pd.DataFrame(data)
    df = pd.concat([df,ddf])
    df.reset_index(drop=True, inplace=True)
    df.to_csv(f'./People_data/{name}_{dic_id}.csv', encoding='utf-8-sig')