import discord
from discord.ext import commands
import os

from help_cog import help_cog
from music_cog import music_cog

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

bot.remove_command('help')

bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))

bot.run("MTAzODU2MTUyOTI0MDQ4NTk0MA.G_1N7y.0Gu86JX6Egb5T-u07vHqtg-XCIhnS_fLxG5SAU")