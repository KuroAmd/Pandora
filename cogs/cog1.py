import discord
from discord.ext import commands
import datetime
#import os
#import pathlib

mood = '~'

class Greetings(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Events
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}!{1}'.format(member,mood))

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = member.guild.system_channel
        print(f'{member} has left a server')
        if channel is not None:
            await channel.send(f"{member} has left the server...")

    #Cmds
    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self.client._last_member is None or self.client._last_member.id != member.id:
            await ctx.send('Hello {0.name}~'.format(member))
        else:
            await ctx.send('Hello {0.name}... Have we met before?'.format(member))
        self._last_member = member
    

#    @commands.command()
#    async def (self,ctx):
        

def setup(client):
    client.add_cog(Greetings(client))