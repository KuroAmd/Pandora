import discord
from discord.ext import commands
import datetime
import random
#import os
#import pathlib

mood = '~'

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Events



    #Cmds

    @commands.command(aliases=['Calc'])
    async def Calculator(self,ctx):
        pass



    @commands.command()
    async def handbook(self,ctx):
        resps = ["**June:**\n > In the final battle, the Souring Devil faction set out to capture Pandora Z in her awakened form. In order to overcome the ultimate weapon, June surrendered control to Bloody Mary, a witch with a lust for chaos and destruction. Just as with me(Pandora) losing her personality in Omega form, June's persona is lost to madness. Now she is the Blood Witch.",
        "**Genbue**\n > Forgot to read about her, sowwy! ><"
        ]
        await ctx.send(f'{random.choice(resps)} ')

    @commands.command(aliases=['say', 'Say'])
    async def _Say(self,ctx, *, msg):
        await ctx.send(f'{msg}')

    @commands.command(hidden=True)
    @commands.has_permissions(administrator=True)
    async def Sayd(self, ctx, *,msg):
        await ctx.channel.purge(limit=1)
        await ctx.send(f"{msg} {mood}")

    @commands.command()
    async def choose(self,ctx, *, choices):
        await ctx.send("{1} choices {0}?".format(len(choices), "or".join(choices)) ,f"Hmm?~\n\n{random.choice(choices)} of course!{mood}")

    @commands.command(aliases=['8ball','question'])
    async def eightball(self,ctx,* ,question):
        responses= ["Yes!",
        "Of course!",
        "Why not?",
        "Sure!",
        "Certainly",
        "100 Percent! \n~~unless my calculations are wrong... which is likely~~",
        "I'd say... Definitely!",
        "There's no doubt about it!",
        "Possible...",
        "Maybe~",
        "Yagita knows!",
        "Don't lose hope~!",
        "Uhh... I'm not sure",
        "I DON'T KNOW! >_<",
        "Very doubtful",
        "I wonder... maybe?",
        "I don't think so",
        "And my answer will be... no",
        "Of course not!",
        "No way",
        "Nah",
        "Nuh-uh!",
        "And no",
        "N O",
        "ahhh My head hurts x_x",
        "Need to think about that... Ask again"]
        await ctx.send(f"You ask: {question}? \nHmm... {random.choice(responses)}")






def setup(client):
    client.add_cog(Fun(client))
