import discord
from discord.ext import commands
import datetime
#import os
#import pathlib

mood = '~'

class Games(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Events


    #Cmds

#    @commands.command()
#    async def (self,ctx):
        



def setup(client):
    client.add_cog(Games(client))