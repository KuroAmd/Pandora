import discord
from discord import Embed
from discord.ext import commands
import google_trans_new
#import random
import datetime

import asyncio
#import py_compile
import pydoc
#import pydoc_data
#import subprocess
#import sys
#import os
import io
import contextlib
#import importlib
#import pickle
#import pprint
import re


class Moderating(commands.Cog):

#   Events



#   Cmds

    class MemberRoles(commands.MemberConverter):
        async def convert(self, ctx, argument):
            member = await super().convert(ctx, argument)
            return [role.name for role in member.roles[1:]] # return roles exluding everyone role!

    @commands.command()
    async def roles(self,ctx, *, roles: MemberRoles = None):
        if roles==None:
            roles=ctx.author
        await ctx.send(f'{ctx.author} they got the following roles: `' + ', '.join(roles) + '`')

    @commands.command(aliases= ["user"])
    async def userinfo(self, ctx, user:discord.User=None):
        if not user:
            user= ctx.author
        em= discord.Embed(title= user.name,url= str(user.avatar_url), description= f"\nHighest role: {user.top_role}\nJoined {user.joined_at}", colour= user.colour)
        em.insert_field_at(0,name= "Name",value= f"{user.mention} (AKA {user.nick})\n\nID: {user.id}")
        em.add_field(name= "Status", value= user.status)
        em.set_thumbnail(url= user.avatar_url)
        em.set_footer(text= "-", icon_url= ctx.author.avatar_url)
        await ctx.send(embed= em)
        

    @commands.command(aliases= ['server'])
    async def serverinfo(self,ctx):
   
        em = discord.Embed(
        title=ctx.guild.name,
        description="description: "+ str(ctx.guild.description) +"\nRules "+ str(ctx.guild.rules_channel) +"\nSystem Channel "+ str(ctx.guild.system_channel),
        colour=discord.Colour.blue())
        em.set_thumbnail(url= ctx.guild.icon_url)
        em.add_field(name="Owner", value=ctx.guild.owner)
        em.add_field(name="Server ID", value=ctx.guild.id)
        em.add_field(name="Region", value=ctx.guild.region)
        em.add_field(name="Member Count", value=ctx.guild.member_count, inline=True)
        em.add_field(name= "Created", value= ctx.guild.created_at)
       # em.add_field(name= "Roles",value= ctx.guild.roles)
        em.add_field(name= "Channel Count", value=len(ctx.guild.channels))
        em.add_field(name="Channels", value= str(len(ctx.guild.text_channels)) +" Text Channels\n"+ str(len(ctx.guild.voice_channels)) +" Voice Channels")

        await ctx.send(embed=em)


    @commands.command(hidden= True)
    #@commands.has_permissions(administrator= True)
    async def Log(self, ctx, num= 1):
      if ctx.author.id == 444806806682730496:
        count= 1
        async for entry in ctx.guild.audit_logs(limit=num):
            print('{0.user} did {0.action} to {0.target}'.format(entry))
            await ctx.send(embed= Embed(title= "last " +str(count), description= "{0.user} did {0.action} to {0.target}".format(entry), colour= discord.Colour.purple()))
            count+= 1
      else:
        print(ctx.author + " attempted to see the logs")

    @commands.command()
    async def findmsg(self,ctx, I:int):
        try:
            ms = await ctx.fetch_message(I)
            await ctx.send(ms)
            print('success')
        except Exception as e:
            print(e)

    @commands.command(aliases=['avatar','av','pfp'])
    async def Avatar(self, ctx, member: discord.User=None):
        if member==None:
            member=ctx.author
        em= Embed(title=member.display_name,
        colour=ctx.author.colour)
        em.set_image(url=member.avatar_url)
        await ctx.send(embed=em)


    @commands.command(hidden=True,aliases=['eval','compute','calc'])
    async def Eval(self, ctx, *,args):
        #await ctx.trigger_typing()
        print(args)
        if ctx.author.id in (444806806682730496 , 435104102599360522):
            await ctx.trigger_typing()
            def python(py_args):
                py_args = (re.search(r"\(.*\)",py_args).group()[1:-1])
                return py_args
            #args = " ".join(args) # this separated every letter!
            #print(args)
            if "help" in args:
                try:
                    x = python(args)
                    y = pydoc.getdoc(eval(x))
                    #print(args)
                    return await ctx.send(embed = discord.Embed(title=f"Help for {x}",description= f"```Python\n{y}```",timestamp=datetime.datetime.utcnow()))
                except Exception as e:
                    return await ctx.send(embed = discord.Embed(tilte="Failure",description=f"```{str(e)}```", timestamp= datetime.datetime.utcnow()))

            try:
                x = await eval(args)
            except Exception as e:
                print(e)
                #await ctx.send(e)
                try:
                    y = eval(args)
                    #print(f"y = {y}")
                    if asyncio.iscoroutine(y):
                        return await ctx.send(embed = discord.Embed(title="Failure.",description=f"{str(y)}",timestamp=datetime.datetime.utcnow()))
                    else:
                        return await ctx.send(embed = discord.Embed(title="Success.",description=f"```{str(y)}```",timestamp=datetime.datetime.utcnow()))
                except Exception as e:
                    print(e)
                    return await ctx.send(embed= discord.Embed(title="Failure",description=str(e), timestamp=datetime.datetime.utcnow()))
            print(f"args = {args}\nx={x}\ty={y}")
            await ctx.send(embed= discord.Embed(title="Success",description=f"```{str(x)}```",timestamp=datetime.datetime.utcnow()))
        
        else:
            await ctx.send("Not allowed to use!")


    @commands.command(aliases=['ec'],hidden=True)
    async def evalcode(self, ctx, *, args):
        await ctx.trigger_typing()
        if ctx.author.id in (444806806682730496 , 435104102599360522):
            client = ctx.bot
            channel = ctx.channel
            content = ctx.message.content.split("```")[1].strip("```")
            if content.startswith("python"):
                content = content.split("python", 1)[1]
            if content.startswith("py"):
                content = content.split("py", 1)[1]
            content = content.replace(r"\n", "\n")
            content = content.replace(r"\t", "    ")
            print(content)
            x = io.StringIO()
            try:
                with contextlib.redirect_stdout(x):
                    exec(content, globals(), locals())
                if x.getvalue():
                    mapping = enumerate(x.getvalue().split("\n"))
                    mapping = list(mapping)[:-1]
                    mult = len(str(len(mapping))) + 1
                   # print(mul)
                    res = "\n".join(map(lambda y: f"{y[0]}.{' ' * (mult - len(str(y[0])))}|{y[1]}", mapping))
                   # print(res)
              
                await ctx.send(f"```python\n{re.sub(r'```', '', res)}```")
            except Exception as e:
                await ctx.send(e)
                return "Error", str(e), "error"
        else:
            await ctx.send("Not allowed!")


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def testin(self,ctx,*, msg):
        '''just owner playing randomly with me'''
        await ctx.message.add_reaction("✅") # reaction intent
      #  if ctx.author.id != :
      #      await ctx.message.add_reaction("❌")
        print(ctx.author, ctx.message, ctx.channel, ctx.channel.id) #works well
        print(ctx.author.id, ctx.message.channel.id, ctx.message.guild)


    @commands.command(aliases=['Purge','purge'])
    @commands.has_permissions(administrator=True)
    async def Prune(self, ctx, amt=10):
        await ctx.trigger_typing()
        await ctx.channel.purge(limit= amt+1)
        await ctx.send(f"there was~~not~~ {amt} messages")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def Prune_Channel(self, ctx):
        await ctx.trigger_typing()
        msgs = await ctx.channel.history(limit=10).flatten()
        print(msgs)
        async for msg in ctx.channel.history(limit=200):
            await ctx.channel.purge(limit=100)
        Bmsg = await ctx.send("Channel Killed")
        await Bmsg.delete(delay=15)

        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def Mute(self, ctx, member:discord.Member, dur=0):
        r = discord.utils.get(ctx.guild.roles, name="Muted")
        print(r)
        if not r:
            r= await ctx.guild.create_role(name="Muted", permissions=discord.Permissions(send_messages=False, change_nickname=False))
            #r= discord.utils.get(ctx.guild.roles, name="Muted")
            print(r)
            bmsg= await ctx.send("mute role created!")
            print(bmsg)
        await member.add_roles(r)
        #await asyncio.sleep(2)
        try:
            await bmsg.delete(delay=2)
        except:
            pass
        if(dur==0):
            await ctx.send(f"{member.mention} has been muted for being naughty")
            return
        await ctx.send(f"{member.mention} is muted for {dur}s!")
        await asyncio.sleep(dur)
        await member.remove_roles(r)
        await ctx.send(f"{member} is now unmuted, behave!{mood}")
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def Kick(self,ctx, member : discord.Member, *, reason=None):
        await member.Kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked outta server")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def Ban(self,ctx, member : discord.Member, *, reason=None):
        await member.Ban(reason=reason)
        await member.send(f"And {member.mention} has been BUNNED")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def Unban(self,ctx, *, member):
        buns= await ctx.guild.bans()
        member_name, member_disc = member.split('#')
        for ban_entry in buns:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_disc):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbunned {user.mention}")
                return


    @commands.command(aliases=['Modding','ModHelp'])
    async def mod_help(self, ctx):
        '''Incomplete...'''
        await ctx.send("uhm...")



def setup(client):
    client.add_cog(Moderating(client))
