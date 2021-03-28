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
    
