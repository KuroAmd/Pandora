import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import random
import datetime
import urllib.parse, urllib.request, re
import aiohttp
import json
import os

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client



    # from somerandomapi doc
    @commands.command()
    async def lyrics(self, ctx, *, arg):
        await ctx.trigger_typing()

        # em = discord.Embed(title=f"**Looking for {arg}...**")

        arg.replace(' ', '+')
        
        lrcsession = aiohttp.ClientSession()
        lrcgetlnk = await lrcsession.get('https://some-random-api.ml/lyrics?title={}'.format(arg))
        lrcdata = json.loads(await lrcgetlnk.text())

        lyrrc = (str(lrcdata['lyrics']))

        try:
            for chunk in [lyrrc[i:i+2000] for i in range(0, len(lyrrc), 2000)]:
                embed = discord.Embed(title=f"**{(str(lrcdata['title']))}** by {(str(lrcdata['author']))}", description=chunk)
                #embed.set_footer(text=chunk)
                embed.set_footer(text="{0}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                #embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)

        except discord.HTTPException:
            embe = discord.Embed(title=f"**{(str(lrcdata['title']))} by {(str(lrcdata['author']))}**", description=chunk)
            embe.set_footer(text="{0}\nID: {1}\n{2}".format(ctx.message.author.name, ctx.message.author.id, datetime.datetime.utcnow().strftime("%A, %B %d %Y at %I:%M:%S %p UTC")), icon_url=ctx.message.author.avatar_url)
            embe.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embe)

        #msg = await ctx.send(embed=em)
    #        await asyncio.sleep(1)
    #        await msg.edit(embed=embed)

        await lrcsession.close()


    # YouTube
    @commands.command(aliases=['yt','Youtube'])
    async def YT(self,ctx, *,search):
        try:
            query_string = urllib.parse.urlencode({
                'search_query': search
            })
            htm_content = urllib.request.urlopen(
                "https://www.youtube.com/results?" + query_string
            )
            search_results=re.findall("href=\"\\/watch\\?v=(.{1})", htm_content.read().decode())
            await ctx.send("https://www.youtube.com/watch?v=" + search_results[0])
        except Exception as e:
            print(e)
            await ctx.send(discord.Embed(title='error',description=e,colour='red'))
# use other method!


def setup(client):
    client.add_cog(Music(client))