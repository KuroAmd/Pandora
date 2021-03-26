import discord
from discord.ext import commands
import random
import datetime
import asyncio
import py_compile
import pydoc
import pydoc_data
import re


class Moderating(commands.Cog):

#   Events



#   Cmds

    class MemberRoles(commands.MemberConverter):
        async def convert(self, ctx, argument):
            member = await super().convert(ctx, argument)
            return [role.name for role in member.roles[1:]] # Remove everyone role!

    @commands.command()
    async def roles(self,ctx, *, member: MemberRoles):
        await ctx.send('{0} got the following roles: '.format(ctx.author) + ', '.join(member))

    @commands.command(aliases=['avatar','av','pfp'])
    async def Avatar(self, ctx, member: discord.Member=None):
        if member==None:
            member=ctx.author
        em= Embed(title=member.display_name,
                colour=ctx.author.colour)
        em.set_image(url=member.avatar_url)
        await ctx.send(embed=em)

        
    @commands.command()
    async def Py(self, ctx, *,args):
        print(args)
        if ctx.author.id == 444806806682730496 or 435104102599360522:
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
            ctx.send("Not allowed to use!")


    @commands.command(aliases=['prune'])
    @commands.has_permissions(administrator=True)
    async def Purge(self, ctx, amt=1):
        await ctx.channel.purge(limit= amt+1)
        await ctx.send(f"{amt} message(s) were deleted~")


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





def setup(client):
    client.add_cog(Moderating(client))
