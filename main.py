import discord
import os
import asyncio
import youtube_dl
import time

# Discord bot Initialization
client = discord.Client(command_prefix='!', intents=discord.Intents.all())

key = os.getenv("DISCORD_TOKEN")


client.run(key)