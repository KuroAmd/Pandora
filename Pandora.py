import discord
from discord.ext import commands , tasks
#import os
from itertools import cycle

mood = '~'
myprefix='*'
client= commands.Bot(commands.when_mentioned_or(myprefix))

status= cycle(["Where is Yagita?","with Yagita","Law of Creation"])
extentions = ['cog1','cog2','cog3','cog4','cog8','cog10']

@client.event
async def on_ready():
    print('Pandora ready~!')
    change_status.start()
@tasks.loop(minutes=40)
async def change_status():
    await client.change_presence(status=discord.Status.idle,activity=discord.Game(next(status)))

@client.event
async def on_disconnect(ctx):
    print("disconnected")
    await ctx.send("GTG")

@client.event
async def on_command_error(ctx, error):
    if (1==0):
        pass

    elif isinstance(error , commands.MissingRequiredArgument):
        await ctx.send("Missing Argument{0}".format(mood))
    

@client.command(hidden=True)
@commands.has_permissions(administrator=True)
async def Load(ctx,extention):
    try:
        client.load_extension('cogs.{0}'.format(extention))
        print('Loaded {0}'.format(extention))
        await ctx.send(f"{extention} added")
    except Exception as error:
        print('{0} error [{1}]'.format(extention,error))

@client.command(hidden=True)
@commands.has_permissions(administrator=True)
async def Unload(ctx,extention):
    try:
        client.unload_extension(f'cogs.{extention}')
        print('unloaded {0}'.format(extention))
        await ctx.send(f"Removed {extention}")
    except Exception as error:
        print('Error: [{1}]'.format(error))

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
async def shutdown(ctx):
    await ctx.send(f"Bye bye{mood}")
    await client.logout()

client.run(os.environ['Disc_Token'])
