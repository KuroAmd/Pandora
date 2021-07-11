import discord
from discord.ext import commands , tasks
import os
from itertools import cycle
import google_trans_new

mood = '~'
myprefix='*'
intents=discord.Intents.all()
h_cmd = commands.DefaultHelpCommand(no_category="Other Commands")

client= commands.Bot(commands.when_mentioned_or(myprefix),intents=intents,help_command=h_cmd)

status= cycle(["Where is Yagita?","with Yagita","Law of Creation"])
extentions = ['cog1','cog2','cog3','cog5','cog8','cog9','cog10']

@client.event
async def on_ready():
    print('Pandora ready~!')
    change_status.start()
@tasks.loop(minutes=40)
async def change_status():
    await client.change_presence(status=discord.Status.online,activity=discord.Game(next(status)))

@client.event
async def on_disconnect(ctx):
	print("disconnected")
	await ctx.send("GTG")

@client.event
async def on_reaction_add(reaction, user):
    print(reaction)
    print(user)
    #print(reaction.message)
    msg = reaction.message.content
    #print(msg)
    #print(self.client)
    if user==client.user:
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

@client.command(hidden=True)
@commands.has_permissions(administrator=True)
async def Load(ctx,extention):
		try:
			client.load_extension('cogs.{0}'.format(extention))
			print('Loaded {0}'.format(extention))
			await ctx.send(f"{extention} added")
		except Exception as error:
			print('{0} error [{1}]'.format(extention,error))
			await ctx.send(embed=discord.Embed(title=f"{extention} error",description=error,colour=16711680))

@client.command(hidden=True)
@commands.has_permissions(administrator=True)
async def Unload(ctx,extention):
		try:
			client.unload_extension(f'cogs.{extention}')
			print('unloaded {0}'.format(extention))
			await ctx.send(f"Removed {extention}")
		except Exception as error:
			print('Error: [{1}]'.format(error))
			await ctx.send(embed=discord.Embed(title=f"{extention} error",description=error,colour=16711680))

@client.command(hidden=True)
@commands.has_permissions(administrator=True)
async def Reload(ctx, extention):
		try:
			client.unload_extension('cogs.{0}'.format(extention))
			client.load_extension('cogs.{0}'.format(extention))
			print('Reloaded {0}'.format(extention))
			await ctx.send("Reloaded")
		except Exception as error:
			await ctx.send(f"Error: [{error}]")
			await ctx.send(embed=discord.Embed(title=f"{extention} error",description=error,colour=16711680))


if __name__ == '__main__':
	for extention in extentions:
		try:
			client.load_extension('cogs.{0}'.format(extention))
			print(f"{extention} loaded")
		except Exception as error:
			print('{0} cannot be loaded [{1}]'.format(extention,error))

@client.command(aliases=['Ping','PING'])
async def ping(ctx):
    await ctx.send(f"Pong{mood}! {round(client.latency *1000)}ms")


@client.command(hidden=True)
@commands.has_permissions(administrator=True)
async def Shutdown(ctx):
    await ctx.send(f"Bye bye{mood}")
    await client.logout()

client.run(os.environ['Pan_Token'])
