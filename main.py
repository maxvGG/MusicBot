import discord
import os

from discord.ext import commands, tasks
import youtube_dl

# Discord bot Initialization
client = discord.Client(intents=discord.Intents.all())
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
key = os.getenv("DISCORD_TOKEN")


client.run(key)