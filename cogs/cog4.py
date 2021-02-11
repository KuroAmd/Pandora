import discord
from discord.ext import commands
import datetime
mood='~'

class spy(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Events

 


@commands.Cog.listener()
async def on_message_delete(self,ctx, msg):
    await ctx.send(msg.channel, 'Message deleted.')



@commands.Cog.listener()
async def on_message(self,msg):
        if msg.author== self.client.user:
            return
        if msg.content.startswith('Hi' or 'Hello' or 'Hey'):
            await msg.channel.send("Hey there!{0} :wave:".format(mood))
        if msg.content.startswith('Bye' or 'bye'):
            await msg.channel.send("Take care!{0}".format(mood))
        if msg.content == 'Send_embed':
            myEmbed = discord.Embed(title="current ver",description="",color=0x00ff00)
            myEmbed.add_field(name="PANDORA",value="v.01",inline=False)
            myEmbed.add_field(name="released date",value='2020',inline=True)
            myEmbed.set_footer(text="Thisisthefooter")
            myEmbed.set_author(name="Unknown")
            await msg.channel.send(embed=myEmbed)
        await self.client.process_commands(msg)





    #commands

#    @commands.command()
#    async def (self,ctx):
        
        

def setup(client):
    client.add_cog(spy(client))