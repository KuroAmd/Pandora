import discord
from discord.ext import commands
import datetime
import google_trans_new


class spy(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Events

 


    @commands.Cog.listener()
    async def on_message_delete(self,ctx, msg):
        bmsg=await ctx.send(msg.channel, 'Message deleted.')
        await bmsg.delete(delay=2)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        print(reaction)
        print(user)
        #print(reaction.message)
        msg = reaction.message.content
        #print(msg)
        #print(self.client)
        if user==self.client.user:
            print("It's my reaction!")
            return
        if str(reaction.emoji)=="🏳️":
            gt = google_trans_new.google_translator()
            tmsg = gt.translate(msg, lang_tgt='en')
            #print(tmsg)
            #print(reaction.message.channel)
            em = Embed(title=msg, description=tmsg, colour=user.colour)
            em.set_footer(text= reaction.message.author.display_name,icon_url=reaction.message.author.avatar_url)
            await reaction.message.channel.send(embed=em)


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
