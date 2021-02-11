import discord
from discord.ext import commands
import random
import datetime

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


    @commands.command(aliases=['prune'])
    @commands.has_permissions(administrator=True)
    async def Purge(self, ctx, amt=1):
        await ctx.channel.purge(limit= amt+1)
        await ctx.send(f"{amt} messages were deleted~")


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