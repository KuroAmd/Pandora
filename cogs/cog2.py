import discord
from discord import Embed
from discord.ext import commands

import datetime
import asyncio

import pydoc

import os
import io
import contextlib

import re
#import wolframalpha
from replit import db


class Moderating(commands.Cog):
    def __init__(self, client):
        self.client = client

    def mee(ctx):## returns True if it's me
      return ctx.author.id==444806806682730496
    def alex(ctx):
      return (ctx.author.id==435104102599360522) or (ctx.author.id==444806806682730496)
    def adminpowa(ctx):
      print(ctx.author)
      if (ctx.author.id==444806806682730496) or (ctx.author.permissions_in(ctx.channel).administrator):
        return True
      else:
        return False
    def aaa(ctx):
      return ctx.author.permissions_in(ctx.channel).administrator
      
#   Test
    @commands.command()
    @commands.check(aaa)
    async def testin(self,ctx,*msg):
        '''just owner playing randomly with me'''
        await ctx.message.add_reaction("✅") #did work! (Intent needs to be on)
        
        bmsg= await ctx.send(f"test {self.client.emojis[3]}")
        await bmsg.add_reaction(self.client.emojis[30])
        #await bmsg.delete(delay=5)
      #  if ctx.author.id == :
      #      await ctx.message.add_reaction("❌")
        print(ctx.author, ctx.message, ctx.channel, ctx.channel.id) #works well
        print(ctx.author.id, ctx.message.channel.id, ctx.message.guild)
        print(ctx.message.reactions)

    @commands.command()
    async def emote(self, ctx, em):
      emt=':no_entry_sign:'
      try:
        emt= self.client.emojis[int(em)]
      except Exception as e:
        print(e)
        for ems in self.client.emojis:
          if re.search(em, ems.name ,re.I):
            emt= ems
      try:
        await ctx.message.delete(delay=1)
      except:
        print("couldn't delete your msg")
      await ctx.send(emt)

#   Events

    @commands.command(aliases=['En','English'],brief="Learn grammar!",hidden=True)
    async def english(self, ctx,tense=None):
        ans = "which tense is that?"
        c= discord.Colour.dark_red()
        if tense.lower()=='past':
            ans = "`use the past form of the verb!` , `subject: who _did_ the verb` , `Object: which the verb is done upon`\n```py\n'Subject' + 'past verb' + 'Object' + 'rest of the sentence'\n```\nthis is Past Simple!\nex: You (Subject) ate (past verb) the cake (Object)"
            c= discord.Colour.orange()
        elif tense.lower()=='present':
            ans = "`use the present form of the verb! (normal form)` , `Subject: who _does_ the verb` , `Object: which the verbs happens upon`\n```py\n'Subject' + 'Verb' + 'Object' + 'rest of the sentence'\n```\nAnd this is the present tense!\nex: The moon (Subject) moves around (verb) the Earth (Object)"
            c=discord.Colour.green()
        elif tense.lower()=='future':
            ans = "it's simple present with *will*\n"
            c=discord.Colour.golden()
        elif tense.lower()=='p':
            ans = "perfect..hmm"
        
        
        await ctx.message.reply(embed=Embed(title=tense, description=ans, colour=c))


#   Cmds

    class MemberRoles(commands.MemberConverter):
        async def convert(self, ctx, argument):
            member = await super().convert(ctx, argument)
            return [role.name for role in member.roles[1:]] # return roles exluding everyone role!

    @commands.command(aliases=["دور","ادوار"])
    async def roles(self,ctx, *, roles: MemberRoles = None):
        if roles==None:
            roles=ctx.author
        await ctx.send(f'{ctx.author}\nthey got the following roles: `' + ', '.join(roles) + '`')

    @commands.command(aliases= ["user","info","مستخدم"])
    async def userinfo(self, ctx, user:discord.User=None):
        if not user:
          user= ctx.author
          print(user)
        #print(type(user))
        des=nick=col=b=None
        if user in ctx.guild.members:
            user = discord.utils.get(ctx.guild.members, id=user.id)
            try:
              des=f"Highest role: {user.top_role}\n\nJoined the server at **{user.joined_at.replace(microsecond=0)}**"
              nick=user.nick
              col=user.colour
            except:
              print("is member but treated as User")
        else:
            des=nick="User is not in the server!"
            col=discord.Colour.dark_gray()
        if user.bot:
          b="Bot"
        else:
          b="discord user"

        em= Embed(title= user.name,url= str(user.avatar_url), description= des, colour= col)
        em.insert_field_at(0,name= "Name",value= f"{user.mention} (AKA {nick})\n\nID: {user.id}")
        em.add_field(name=f"{b} Account",value= f"since {user.created_at.replace(microsecond=0)}")
        if user in ctx.guild.members:
          try:
            em.add_field(name="Activity",value=user.activity)
            em.add_field(name= "Status", value= user.status)
          except:
            pass
        em.set_thumbnail(url= user.avatar_url)
        em.set_footer(text= "-", icon_url= ctx.author.avatar_url)
        try:
          em.add_field(name=user.public_flags)
        except:
          pass
        await ctx.send(embed= em)
        
    @commands.command(aliases= ['server','Info',"خادم"])
    async def serverinfo(self,ctx):
        em = Embed(title=ctx.guild.name, description=f"description: {str(ctx.guild.description)}\nRules {str(ctx.guild.rules_channel)}\nSystem Channel {str(ctx.guild.system_channel)}", colour=discord.Colour.blue())
        em.set_thumbnail(url= ctx.guild.icon_url)
        em.add_field(name="Owner", value=ctx.guild.owner)
        em.add_field(name="Server ID", value=ctx.guild.id)
        em.add_field(name="Region", value=ctx.guild.region)
        em.add_field(name="Member Count", value=ctx.guild.member_count, inline=True)
        em.add_field(name= "Created", value= ctx.guild.created_at)
        em.add_field(name= "Roles",value= len(ctx.guild.roles))
        em.add_field(name="Channels", value= f"Total channels ={len(ctx.guild.channels)} \n{str(len(ctx.guild.text_channels))} Text Channels\n {str(len(ctx.guild.voice_channels))} Voice Channels")
        em.add_field(name='extras',value=f"verification lvl: {ctx.guild.verification_level}\nCategories= {len(ctx.guild.categories)}\nBoosters: {ctx.guild.premium_subscribers}")

        await ctx.send(embed=em)


    @commands.command(aliases=["لوگ"],hidden= True)
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
        '''Incomplete...'''
        try:
            ms = await ctx.fetch_message(I)
            await ctx.send(ms)
            print('success')
        except Exception as e:
            print(e)

    @commands.command(aliases=['avatar','av','pfp',"بروفايل","صورة"])
    async def Avatar(self, ctx, u: discord.User=None):
        if u==None:
            u=ctx.author
        em= Embed(title=u.display_name,
        colour=u.colour)
        em.set_image(url=u.avatar_url)
        await ctx.send(embed=em)


    @commands.command(hidden=True,aliases=['eval','compute','calc',"حساب","حاسبة"])
    @commands.check(mee)
    async def Eval(self, ctx, *,args):
        #await ctx.trigger_typing()
        print(args)
        if ctx.author.id in (444806806682730496 , 435104102599360522):# should I remove this condition?
            await ctx.trigger_typing()
            def python(py_args):
                py_args = (re.search(r"\(.*\)",py_args).group()[1:-1])
                return py_args
            #args = "".join(args) # this separated every letter!
            #print(args)
            if "help" in args:
                try:
                    args= args.strip("help")
                    print(args)
                    print("get to help page")
                    x = python(args)
                    print('x= ',x)
                    y = pydoc.getdoc(x)
                    print('y= ',y)
                    z=pydoc.getdoc(eval(x))
                    print(f"Z= {z}")
                    return await ctx.send(embed = Embed(title=f"Help for {x}", description= f"```Python\n{z}```", colour=discord.Colour.blurple() ,timestamp=datetime.datetime.utcnow()))
                except Exception as e:
                    return await ctx.send(embed = Embed(tilte="Failure", description=f"```{str(e)}```", timestamp= datetime.datetime.utcnow(),colour=discord.Colour.red()))

            try:
                x = await eval(args)
            except Exception as e:
                print(e)
                await ctx.send(e)
                try:
                    y = eval(args)
                    #print(f"y = {y}")
                    if asyncio.iscoroutine(y):
                        return await ctx.send(embed = Embed(title="Failure.",description=f"{str(y)}",timestamp=datetime.datetime.utcnow(),colour=56550))
                    else:
                        return await ctx.send(embed = Embed(title="Success.",description=f"```{str(y)}```",timestamp=datetime.datetime.utcnow(),colour=56550))
                except Exception as e:
                    print(e)
                    return await ctx.send(embed= discord.Embed(title="Failure",description=str(e), timestamp=datetime.datetime.utcnow(),colour=discord.Colour.red()))
            print(f"args = {args}\nx={x}\ny={y}")
            await ctx.send(embed= discord.Embed(title="Success",description=f"```{str(x)}```",colour=56550,timestamp=datetime.datetime.utcnow()))
        
        else:
            await ctx.send("Not allowed to use!")


    @commands.command(aliases=['ec'],hidden=True)
    @commands.check(mee)
    async def evalcode(self, ctx, *, args):
      await ctx.trigger_typing()
      if ctx.author.id == 444806806682730496:# now no need for this condition
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

              ## commented if -
              #if x.getvalue():
              mapping = enumerate(x.getvalue().split("\n"))
              mapping = list(mapping)[:-1]
              mult = len(str(len(mapping))) + 1
              # print(mul)
              res = "\n".join(map(lambda y: f"{y[0]}.{' ' * (mult - len(str(y[0])))}|{y[1]}", mapping))
              # print(res)

              await ctx.send(f"```python\n{re.sub(r'```', '', res)}```")
              ## and returned above lines instead

              #else:
              #  await ctx.send(embed=Embed(title="error :/",description="```py\nx.getvalue()``` didn't work", colour=discord.Colour.red()))
          except Exception as e:
              await ctx.send(e)
              em= Embed(title="Error",description=e,colour=discord.Colour.red())
              await ctx.send(embed=em)
              #return "Error", str(e), "error"
      else:
          await ctx.send("Not allowed!")


    @commands.command(aliases=['Purge','purge',"محو"])
    @commands.check(adminpowa)
    async def Kill(self, ctx, amt=10):
        await ctx.trigger_typing()
        await ctx.channel.purge(limit= amt+1)
        await ctx.send(f"{amt} souldregs were killed ")

    @commands.command()
    @commands.check(adminpowa)
    async def Kill_all(self, ctx):
        await ctx.trigger_typing()
        msgs = await ctx.channel.history(limit=10).flatten()
        print(msgs)
        async for msg in ctx.channel.history(limit=200):
            await ctx.channel.purge(limit=100)
        Bmsg = await ctx.send("Channel Killed")
        await Bmsg.delete(delay=12)

    @commands.command(aliases=["اسکات"])
    @commands.check(adminpowa)
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
        await ctx.send(f"{member} is now unmuted, behave!")

    @commands.command(aliases=["طرد"])
    @commands.check(adminpowa)
    async def Kick(self,ctx, member : discord.Member, *, reason=None):
        await member.Kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked outta server")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def Ban(self,ctx, member : discord.Member, *, reason=None):
        await member.Ban(reason=reason)
        await member.send(f"And {member.mention} has been BUNNED")

    @commands.command()
    @commands.check(adminpowa)
    async def Unban(self,ctx, *, member):
        buns= await ctx.guild.bans()
        member_name, member_disc = member.split('#')
        for ban_entry in buns:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_disc):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbunned {user.mention}")
                return


    @commands.command(hidden=True)
    @commands.check(mee)
    async def Intent(self, ctx, i,b=None):
      try:
        member_spy = db["member_spy"]
        mylog = db["mylog"]
      except Exception as e:
        print(e)
        await ctx.send('no previous keys')
        db["member_spy"]=None
        db["mylog"]= None
      await ctx.message.delete()
      if i=='member':
        if b=='on':
          member_spy =True
        else:
          member_spy =False
        await ctx.send(f"set value {member_spy}")
      elif i=='logs':
        try:
          mylog=discord.utils.get(ctx.guild.text_channels,id=b)
          print(mylog.name)
        except Exception as e:
          print(e)
          try:
            mylog=discord.utils.get(ctx.guild.text_channels,name=b)
            print(mylog.name)
          except Exception as e:
            print(e)
            #await ctx.send(content=e,delete_after=3)
            try:
              b:discord.TextChannel
              if not isinstance(b,discord.TextChannel):
                raise Exception("b is not a channel type")
              mylog=b
            except Exception as e:
                print(e)
                mylog=None
                await ctx.send(content="log is turned off",delete_after=4)
        await ctx.send(f"logs channel set to {mylog.mention} in {mylog.category}")

      else:
        await ctx.send("{0}??".format(db['mood']))
      db["member_spy"] = member_spy
      db["mylog"] = mylog


def setup(client):
    client.add_cog(Moderating(client))
