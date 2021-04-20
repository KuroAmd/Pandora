import discord
from discord.ext import commands
import datetime
#import os
import asyncio

mood = '~'

class CustomCmds(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Events

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            Bmsg = await ctx.send("I don't understand, is that a new command?")
            await asyncio.sleep(3)
            await Bmsg.delete()






    #commands

#    @commands.command()
#    async def (self,ctx):
        

def setup(client):
    client.add_cog(CustomCmds(client))
