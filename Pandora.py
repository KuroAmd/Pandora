import random
import os
#import json
import discord
from discord.ext import commands

Pan = commands.Bot(command_prefix='*')
mood = '~'

@Pan.event
async def on_ready():
    print("Pandora is on!")
    await Pan.change_presence(activity=discord.Game(name="with Yagita"))
    
@Pan.event
async def on_member_join(member):
    print(f'{member} has joined my family!~ :PDRpan_yay1:')
#    await member.channel.send(f"{member} has joined my family!~ :PDRpan_yay1:")

@Pan.event
async def on_member_remove(member):
    print(f'{member} has left the family... :PDRpan_no1:')
#    await member.channel.send(f"{member} has left the family... :PDRpan_no1:")

#@Pan.event
#async def on_message(msg):
#    if msg.content.startswith('Hi' or 'Hello' or 'Hey'):
#        await msg.channel.send("Hey there!{0} :wave:".format(mood))
#    if msg.content.startswith('Bye' or 'bye'):
#        await msg.channel.send("Take care!{0}".format(mood))

@Pan.command(aliases=['say', 'Say'])
async def _Say(ctx, *, msg):
    await ctx.send(f'{msg}{mood}')

@Pan.command()
async def ping(ctx):
    await ctx.send(f'Pong!{mood} {round(Pan.latency * 1000)}ms')

@Pan.command()
async def choose(ctx, c1, c2):
    choices =[c1, c2]
    await ctx.send(f'{c1}? or {c2}? Hmm?~\n\n{random.choice(choices)} of course!{mood}')

@Pan.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['Yes!',
    'No!',
    'I don\'t know.',
    'Prbably.',
    'it is possible!',
    'Yagita knows!',
    'Don\'t lose hope!',
    'Let me think... Ask again later please.',
    'Nuh-uh!',
    'Sure!',
    'Without a doubt!']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}{mood}')

@Pan.command()
async def shred(ctx, amt=3):
    await ctx.channel.purge(limit=amt)
    await ctx.send(f'{amt} messages were shredded.{mood}')

@Pan.command(aliases=['prune', 'purge'])
async def Prune_guide(ctx):
    await ctx.send("To make me prune/purge(delete number of messages)\nUse *shred (amount)\n`if the amount of messages isn't determined, I will delete 3!`")

@Pan.command()
async def handbook(ctx):
    resps = ["**June:**\n > In the final battle, the Souring Devil faction set out to capture Pandora Z in her awakened form. In order to overcome the ultimate weapon, June surrendered control to Bloody Mary, a witch with a lust for chaos and destruction. Just as with me(Pandora) losing her personality in Omega form, June's persona is lost to madness. Now she is the Blood Witch."


    ]
    await ctx.send(f'{random.choice(resps)} ')

@Pan.command(name='halp')
async def _help(ctx):
    await ctx.send("`My prefix is *` \n```css\n(unavailable)I will greet newcomers! As part of our family!\nAnd say goodbyes to the ones leaving ;-;\n```My commands for now are:```Say (message) , ping , 8ball (question) , handbook```\n`I don't know much yet, but @KillerAmd#3312 taught me few tricks for now! :D`")

@Pan.command()
async def mode(ctx, value):
    global mood
    if value == '0':
        mood = "~"
    if value == '1':
        mood = " nya~"
    await ctx.send("My mood changed!{0}".format(mood))

@Pan.command()
async def shutdown(ctx):
    await ctx.send(f"Bye bye{mood}")
    await Pan.logout()

Pan.run(os.environ['Disc_Token'])
