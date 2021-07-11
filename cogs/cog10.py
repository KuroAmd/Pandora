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
          await Bmsg.delete(delay=3)
          return
        print(error)
        await ctx.send(embed=discord.Embed(title='Error', description=f'{error}', colour=16711680))



    #commands

#    @commands.command()
#    async def (self,ctx):
        

def setup(client):
    client.add_cog(CustomCmds(client))
