import discord
from discord.ext import commands
import random
import datetime


class LoC(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self._last_member = None


    @commands.command()
    async def handbook(self,ctx):
        resps = ["**June:**\n > In the final battle, the Souring Devil faction set out to capture Pandora Z in her awakened form. In order to overcome the ultimate weapon, June surrendered control to Bloody Mary, a witch with a lust for chaos and destruction. Just as with me(Pandora) losing her personality in Omega form, June's persona is lost to madness. Now she is the Blood Witch.",
        "**Genbue**\n > Forgot to read about her, sowwy! ><"
        ]
        await ctx.send(f'{random.choice(resps)} ')



def setup(client):
    client.add_cog(LoC(client))
    
#from discordpy
#class Greetings(commands.Cog):
#    def __init__(self, bot):
#        self.bot = bot
#        self._last_member = None

#    @commands.Cog.listener()
#    async def on_member_join(self, member):
#        channel = member.guild.system_channel
#        if channel is not None:
#            await channel.send('Welcome {0.mention}.'.format(member))

#    @commands.command()
#    async def hello(self, ctx, *, member: discord.Member = None):
#        """Says hello"""
#        member = member or ctx.author
#        if self._last_member is None or self._last_member.id != member.id:
#            await ctx.send('Hello {0.name}~'.format(member))
#        else:
#            await ctx.send('Hello {0.name}... Have we met before?'.format(member))
#        self._last_member = member
