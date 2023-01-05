import discord, requests
from discord.ext import commands

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("bot started")

@bot.command()
async def send(ctx, *, question):
    rd = requests.session()
    r = rd.get(f"https://alsh-bg.ml/api/instagram/x.php?url={question}").json()['data']
    #user = ctx.author
    for i in r:
        await ctx.send(i['url'])

bot.run('MTA1ODMzMjE0ODUwNTAwMjAxNA.GXDNFU.nCh-iJH0XuN4s8rlqu7lW5CbrSjtAxkr55-JYE')
