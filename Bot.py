#Budge the Judge ~ by ~ Gytis

#Imports
import discord.utils
import discord
import asyncio
import random
import json
import os
from discord_buttons import DiscordButton, Button, ButtonStyle, InteractionType
from discord.ext import commands
from discord.utils import get

#Vars
client = commands.Bot(command_prefix = '!', intents=discord.Intents.all())
os.chdir("D:\Budge the Judge")
client.remove_command('help')
ddb = DiscordButton(client)

#Def
def dev(ctx):
    return ctx.author.id in [301014178703998987, 289211621845237760]
    #Me, Jamm

#Events
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="!help"))
    print('Budge the Judge now online!')

@client.event
async def on_message(msg):
    if msg.content == "!buttontest":
        m = await msg.channel.send(
            "Stuff request idk",
            buttons = [
                Button(style=ButtonStyle.green, label="Sure"),
                Button(style=ButtonStyle.gray, label="Ignore.."),
                Button(style=ButtonStyle.red, label="Nah"),
            ],
        )

        res = await ddb.wait_for_button_click(m)
        await res.respond(
            type=InteractionType.ChannelMessageWithSource,
            content=f'{res.button.label} clicked'
        )
    await client.process_commands(msg)

#Commands
@client.command()
async def stats(ctx):
    with open('db.json') as f:
        data = json.load(f)
        userid = f"{ctx.author.id}"
        await ctx.send(f"**Money:**             {data[f'{userid}']['money']}\n**Population:**      {data[f'{userid}']['population']}\n**Happiness:**      {data[f'{userid}']['happy']}\n**Level:**                {data[f'{userid}']['level']}")

@client.command()
async def create(ctx):
    with open('db.json', 'r+') as f:
        data = json.load(f)
        userid = f"{ctx.author.id}"
        data[f"{userid}"] = {
            "money": "0",
            "population": "0",
            "happy": "0",
            "level": "0"
        }
        f.seek(0)
        f.truncate()
        json.dump(data, f, indent=4)

@client.command()
async def reset(ctx):
    with open('db.json', 'r+') as f:
        data = json.load(f)
        userid = f"{ctx.author.id}"
        data[f'{userid}']['money'] = "0"
        f.seek(0)
        f.truncate()
        json.dump(data, f, indent=4)
        data[f'{userid}']['population'] = "0"
        f.seek(0)
        f.truncate()
        json.dump(data, f, indent=4)
        data[f'{userid}']['happy'] = "0"
        f.seek(0)
        f.truncate()
        json.dump(data, f, indent=4)
        data[f'{userid}']['level'] = "0"
        f.seek(0)
        f.truncate()
        json.dump(data, f, indent=4)

@client.command()
async def start(ctx):
    with open('db.json') as f:
        data = json.load(f)
        userid = f"{ctx.author.id}"
        if data[f'{userid}']['money'] == "0" and data[f'{userid}']['population'] ==  "0" and data[f'{userid}']['happy'] == "0" and data[f'{userid}']['level'] == "0":
            await ctx.send("start")
        else:
            await ctx.send("Please reset your current thing to start")

#Run Token
client.run('OTI3NzMwNzQxNTI4Mzk1ODA2.YdOelQ.PBwO6lE5K0nwnVeAv-tdguwxiAY')