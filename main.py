# to access the .env
from decouple import config
import discord
from discord.ext import commands
import music

client = commands.Bot(command_prefix='?', intents= discord.Intents.all())

cogs = [music]
for i in range (len(cogs)):
    cogs[i].setup(client)



client.run(config('KEY'))