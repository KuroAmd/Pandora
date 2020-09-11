import random
import os
import json
import discord
from discord.ext import commands
p='*'
Pan = commands.Bot(command_prefix=p)
mood = '~'
#os.chdir('KuroAmd/')
@Pan.event
async def on_ready():
    print("Pandora is on!")
    await Pan.change_presence(activity=discord.Game(name="with Yagita"))
@Pan.event
async def on_member_join(member):
    print(f'{member} has joined my family!~ :PDRpan_yay1:')
    await member.channel.send(f"{member} has joined my family!~ :PDRpan_yay1:")
@Pan.event
async def on_member_remove(member):
    print(f'{member} has left the family... :PDRpan_no1:')
    await member.channel.send(f"{member} has left the family... :PDRpan_no1:")
@Pan.command(aliases=['say', 'Say'],description="I'll say what you say!")
async def _Say(ctx, *, msg):
    await ctx.send(f'{msg}{mood}')
@Pan.command(description='Latency')
async def ping(ctx):
    await ctx.send(f'Pong!{mood} {round(Pan.latency * 1000)}ms')
@Pan.command(description='I will choose for you between two things')
async def choose(ctx, c1, c2):
    choices =[c1, c2]
    await ctx.send(f'{c1}? or {c2}? Hmm?~\n\n{random.choice(choices)} of course!{mood}')
@Pan.command(name='8ball',description='Ask me any question!')
async def _8ball(ctx, *, question):
    responses = ['Yes!',
    'No!',
    'I don\'t know.',
    'Prbably.',
    'Maybe',
    'Can you reconstruct the question?',
    'it is possible!',
    'Yagita knows!',
    'Don\'t lose hope!',
    'Let me think... Ask again please.',
    'Nuh-uh! ',
    'Sure!',
    'Without a doubt!']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}{mood}')
@Pan.command(hidden=True)
async def shred(ctx, amt=3):
    if author.permissions(administrator):
        await ctx.channel.purge(limit=amt)
        await ctx.send(f'{amt} messages were shredded.{mood}')
    else:
        await ctx.send("access denied!{0}".format(mood))
@Pan.command(aliases=['prune', 'purge'])
async def Prune_guide(ctx):
    await ctx.send("To make me prune/purge(delete number of messages)\nUse *shred (amount)\n`if the amount of messages isn't determined, I will delete 3!`")
@Pan.command(description='About Law of Creation characters')
async def handbook(ctx):
    resps = ["**June:**\n > In the final battle, the Souring Devil faction set out to capture Pandora Z in her awakened form. In order to overcome the ultimate weapon, June surrendered control to Bloody Mary, a witch with a lust for chaos and destruction. Just as with me(Pandora) losing her personality in Omega form, June's persona is lost to madness. Now she is the Blood Witch."


    ]
    await ctx.send(f'{random.choice(resps)} ')
@Pan.command(name='halp',description='Let me explain what I can do')
async def _help(ctx):
    await ctx.send(f"`My prefix is` **`{p}`** \n\nMy commands for now are:```Say (message) \n choose (choice_1) (choice_2) \n ping \n 8ball (question) \n handbook```\n`I don't know much yet, but @KillerAmd#3312 taught me few tricks for now! :D`")
@Pan.command()
async def mode(ctx, value):
    global mood
    if value == '0':
        mood = "~"
    if value == '1':
        mood = " nya~"
    await ctx.send("My mood changed!{0}".format(mood))
@Pan.command(hidden=True)
async def shutdown(ctx):
    if author.id == 444806806682730496:
        await ctx.send(f"Bye bye{mood}")
        await Pan.logout()

'''#lvling sys (json)
@Pan.event
async def on_message(message):
    if message.author==Pan.user:
        return
    with open('usersdata.json','r') as f:
        users = json.load(f)
    await update_data(users, message.author)
    await add_exp(users, message.author,5)
    await lvl_up(users, message.author, message.channel)
    with open('usersdata.json','w') as f:
        json.dump(users,f)
    await Pan.process_commands(message)
async def update_data(users, user):
    if not str(user.id) in users:
        users[str(user.id)]={}
        users[str(user.id)]['experience']=0
        users[str(user.id)]['level']=1
        users[str(user.id)]['wallet']=1000
async def add_exp(users,user,exp):
    users[str(user.id)]['experience'] += exp
    users[str(user.id)]['wallet'] += (exp*5)
async def lvl_up(users, user, channel):
    experience = users[str(user.id)]['experience']
    lvl_start = users[str(user.id)]['level']
    lvl_end = int(experience ** (1/4))
    if lvl_start < lvl_end:
        await channel.send_message(f"Congratulation! {user.mention}, You've leveled up to {lvl_end}!")
        users[str(user.id)]['level']= lvl_end
'''

Pan.run(os.environ['Disc_Token'])
