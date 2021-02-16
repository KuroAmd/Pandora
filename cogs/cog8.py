import discord
from discord.ext import commands
from discord import Embed
import datetime
import random
from aiohttp import request
#import os
#import pathlib

mood = '~'

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Events



    #Cmds


    @commands.command(aliases=['Calc'])
    async def Calculator(self,ctx,*,equation):
        ans=equation
        await ctx.send(f"Answer= {ans}")


    @commands.command(aliases=['animalfact','anifact','afact'])
    async def animal(self,ctx, animal: str):
        if animal.lower() in ("dog","cat","panda","fox","bird","koala"):
            fact_URL= f"https://some-random-api.ml/facts/{animal.lower()}"
            img_URL= f"https://some-random-api.ml/img/{'birb' if animal.lower()=='bird' else animal.lower()}"

            async with request("GET",img_URL,headers={}) as response:
                if response.status==200:
                    data= await response.json()
                    img_link=data["link"]

            async with request("GET",fact_URL,headers={}) as response:
                if response.status == 200:
                    data = await response.json()

                    embed=Embed(title=f"{animal.title()} fact",
                                description=data["fact"],
                                colour = ctx.author.colour)
                    embed.set_image(url=img_link)
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"API returned: {response.status}")
        else:
            await ctx.send(f"Nothing found for {animal.lower()}")


    @commands.command(aliases=['Wink'])
    async def wink(self,ctx):
        async with request("GET","https://some-random-api.ml/animu/wink",headers={}) as response:
            if response.status==200:
                data=await response.json()
                ImgLink=data["link"]
                myembed=Embed(title=f"{ctx.author} winks")
                myembed.set_image(url=ImgLink)
                await ctx.send(embed=myembed)
            else:
                await ctx.send("API returned: {0.status}".format(response))

    @commands.command(aliases=['Pat'])
    async def pat(self,ctx,player=None):
        async with request("GET","https://some-random-api.ml/animu/pat",headers={}) as response:
            if response.status==200:
                data=await response.json()
                ImgLink=data["link"]
                if (player==None):
                    myembed=Embed(title=f"pats {ctx.author.display_name}")
                    myembed.set_image(url=ImgLink)
                else:
                    myembed=Embed(title=f"{ctx.author} pats {player.display_name}")
                    myembed.set_image(url=ImgLink)
                await ctx.send(embed=myembed)
            else:
                await ctx.send("API returned: {0.status}".format(response))

    @commands.command(aliases=['Hug'])
    async def hug(self,ctx,player=None):
        async with request("GET","https://some-random-api.ml/animu/hug",headers={}) as response:
            if response.status==200:
                data=await response.json()
                ImgLink=data["link"]
                if (player==None):
                    myembed=Embed(title=f"hugs {ctx.author.display_name}")
                    myembed.set_image(url=ImgLink)
                else:
                    myembed=Embed(title=f"{ctx.author} hugs {player.display_name}")
                    myembed.set_image(url=ImgLink)
                await ctx.send(embed=myembed)
            else:
                await ctx.send("API returned: {0.status}".format(response))

    @commands.command(aliases=['Meme','Memes','memes','MEME','MakeMeLaugh','LOL'])
    async def meme(self,ctx):
        async with request("GET","https://some-random-api.ml/meme",headers={}) as response:
            if response.status==200:
                data=await response.json()
                ImgLink=data["image"]
                Cap=data["caption"]
                Categ=data["category"]
                myembed=Embed(title=f"{Cap}",description=f"{Categ}")
                myembed.set_image(url=ImgLink)
                await ctx.send(embed=myembed)
            else:
                await ctx.send("API returned: {0.status}".format(response))


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
