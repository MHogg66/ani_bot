import discord
import requests
import json
from random import randint

from discord.ext import commands

client = commands.Bot(command_prefix=">")


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.command(brief='random animeme')
async def animeme(ctx):
    try:
        res = requests.get('https://json.reddit.com/r/animemes/new/', headers={'User-Agent': 'Mozilla/5.0'})
        data = json.loads(res.text)['data']
        post = data['children'][randint(0, int(data['dist']) - 1)]['data']
        image = discord.Embed(title=post['title'])
        image.set_image(url=post['url_overridden_by_dest'])
        await ctx.send(embed=image)
    except:
        await ctx.send('no animemes :(')

client.run('') # bot secret here :)