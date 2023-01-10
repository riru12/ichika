import discord
import json
from discord.ext import commands
from dotenv import dotenv_values

TOKEN = dotenv_values(".env")["DISCORD_TOKEN"]

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Booting...")

@bot.command()
async def help(ctx):
    # fetching of data from ichika.json
    jsonFile = open("ichika.json", "r")
    data = json.load(jsonFile)
    jsonFile.close()

    helpDesc=data["help"]["desc"]
    helpCommands=data["help"]["commands"]

    # embed formatting
    embed=discord.Embed(title="Ichika Commands", description=helpDesc)
    embed.add_field(name="Command List", value=helpCommands, inline=False)
    embed.set_footer(text="Bot written by riru#7618")

    await ctx.send(embed=embed)


@bot.command()
async def hello(ctx):
    await ctx.send("Hi!")

@bot.command()
async def add(ctx, a, b):
    await ctx.send(f"{a} + {b} = {str(int(a)+int(b))}")

@bot.command()
async def labyu(ctx):
    await ctx.send("labyu too")

@bot.command()
async def angry(ctx):
    # fetching of data from ichika.json
    jsonFile = open("ichika.json", "r")
    data = json.load(jsonFile)
    jsonFile.close()

    # not yet working
    data["angry"]["count"] = str(int(data["angry"]["count"])+1)

    # writing of data to ichika.json
    jsonFile = open("ichika.json", "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()

    # print angry count
    angryCount = data["angry"]["count"]
    await ctx.send(f"Angry count: {angryCount}")

bot.run(TOKEN)