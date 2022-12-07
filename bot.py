import discord
from dotenv import dotenv_values

client = discord.Client(intents=discord.Intents.default())
TOKEN = dotenv_values(".env")["DISCORD_TOKEN"]

@client.event
async def on_ready():
    print("Bot is now online.")

client.run(TOKEN)