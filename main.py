# to access the .env
import os

from decouple import config
import discord
from discord.ext import commands
import music

client = commands.Bot(command_prefix='?', intents=discord.Intents.all())

cogs = [music]
for i in range(len(cogs)):
    cogs[i].setup(client)

client.run(os.getenv("DISCORD_TOKEN"))
