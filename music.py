import discord
from discord.ext import commands
import youtube_dl


class Music(commands.Cog):
    def __int__(self, client):
        self.client = client


def setup(client):
    client.add_cog(Music(client))
