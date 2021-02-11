import discord
from discord.ext import commands
import datetime
#import os
#import pathlib

mood = '~'

class CustomCmds(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Events

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("I don't understand what I should do, is that a new command?")






    #commands

#    @commands.command()
#    async def (self,ctx):
        

def setup(client):
    client.add_cog(CustomCmds(client))