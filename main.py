# to access the .env
from decouple import config

import discord
from discord.ext import commands

client = commands.Bot(command_prefix='?', intents= discord.Intents.all())

client.run(config('KEY'))