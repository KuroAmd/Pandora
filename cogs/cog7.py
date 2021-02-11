import discord
from discord.ext import commands
import json

class Lvling:
    def __init__(self, bot):
        self.bot =bot

        self.bot.loop.create_task(self.save_users())
        with open(r"D:\Programs0\Projects\Discord Bots\PANDORA\cogs\data07.json",'r') as f:
            self.users = json.load(f)

    async def save_users(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            with open(r"D:\Programs0\Projects\Discord Bots\PANDORA\cogs\data07.json",'w') as f:
                json.dump(self.users, f, indent=4)
    def lvlup(self, author_id):
        xp_now=self.users[author_id]['exp']
        lvl_now=self.users[author_id]['level']

        if xp_now>= round((4*(lvl_now**3))/5):
            self.users[author_id]['level']+=1
            return True
        else:
            return False

            


    async def on_message(self, message):
        if message.author== self.bot.user:
            return
        author_id= str(message.author.id)

        if not author_id in self.users:
            self.users[author_id]= {}
            self.users[author_id]['level']=1
            self.users[author_id]['exp']=0

        self.users[author_id]['exp']+=50


def setup(bot):
    bot.add_cog(Lvling(bot))
