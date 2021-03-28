import discord
from discord.ext import commands
from discord import Embed
import datetime
import random
import aiohttp
from aiohttp import request
import urllib.parse, urllib.request, re
import io
#import os
#import pathlib

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        res = await session.get(url)
        html = await res.text()
        return html

mood = '~'

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Events



    #Cmds


#not working
#    @commands.Cog.listener()
#    async def on_command_error(self,ctx,error):
#        await ctx.send(f"Uhm... Don't laugh! but I can't do math\n {error}")


    @commands.command(aliases=['CERN'])
    async def CernNews(self, ctx):
        await ctx.trigger_typing()


        website = "https://home.cern/news?audience=23"
        html_text = await fetch(website)
        soup = BeautifulSoup(html_text, 'lxml')
        news = soup.find_all('div',class_='views-row')
        
        for n in news:
            try:
                headlines = n.find('h3', class_='preview-list-title').text
            except:
                print("error01")
                continue
            try:
                description = n.find('div', class_='preview-list-strap').text
                news_date = n.find('div', class_='preview-list-date has-separator').text
                more_info = ("https://home.cern" + n.h3.a['href'])
            except:
                print("something went wrong")
                await ctx.send("err")
            if(headlines != None):
                break

        await ctx.send(f'''
headlines: {headlines.strip()}
description: {description.strip()}
date: {news_date.strip()}\n
look in {more_info}
        ''')


    @commands.command()
    async def wasted(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.author

        
        wastedsession = aiohttp.ClientSession()
        async with wastedsession.get(f"https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format='png')}") as img:
            if img.status != 200:
                await ctx.send("Unable to get image")
                await wastedsession.close()      
            else:
                data = io.BytesIO(await img.read())
                await ctx.send(file=discord.File(data, 'wasted.png'))
                await wastedsession.close()


    @commands.command(aliases=['animalfact','afact'])
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


    @commands.command(aliases=['say', 'Say'])
    async def repeatafterme(self,ctx, *, msg):
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
        await ctx.send(f"You ask: {question}? \n {random.choice(responses)}")






def setup(client):
    client.add_cog(Fun(client))
