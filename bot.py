import discord, json, datetime
from discord.ext import commands
from dotenv import dotenv_values
import os
from scidownl import scihub_download


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
    # command only works for ARIA_ID
    if (ctx.author.id == int(dotenv_values(".env")["ARIA_ID"])):
        await ctx.send("labyu too")

@bot.command()
async def angry(ctx):
    # fetching of data from ichika.json
    jsonFile = open("ichika.json", "r")
    data = json.load(jsonFile)
    jsonFile.close()

    # fetch values from data, then modify for printing later
    angryCount = str(int(data["angry"]["count"])+1)
    notAngryTime = ctx.message.created_at.timestamp() - data["angry"]["lastused"]
    notAngryTime_formatted = str(datetime.timedelta(seconds=notAngryTime)).split(".")[0]

    # updating of angry count and lastused
    data["angry"]["count"] = str(int(data["angry"]["count"])+1)
    data["angry"]["lastused"] = ctx.message.created_at.timestamp()

    # writing of data to ichika.json
    jsonFile = open("ichika.json", "w+")
    jsonFile.write(json.dumps(data, indent=4))
    jsonFile.close()

    # print angry count
    await ctx.send(f"Angry count: **{angryCount}**\nTime since was last angry: **{notAngryTime_formatted}**")

@bot.command()
async def scidl(ctx, *, search_entry: str):
    paper = search_entry
    paper_type = "title"
    out = "./papers/"+search_entry+".pdf"
    proxies = {
        'http': 'socks5://127.0.0.1:7890'
    }
    try:
        scihub_download(paper, paper_type=paper_type, out=out, proxies=proxies) # download the paper
        if os.path.exists(out):
            await ctx.send(f"Paper retrieved: **{search_entry}**")
            await ctx.send(file=discord.File(out)) # upload on discord
            os.remove(out) # delete the file after it has been uploaded
        else:
            raise Exception('error')
    except:
         await ctx.send("There was an error in downloading the paper. This paper either **(a)** does not exist, **(b)** is not found in the sci-hub database, **(c)** or something went wrong - please try again.")

bot.run(TOKEN)