import discord
from discord.ext import commands
import datetime
import random
#import pathlib


class Games(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Events


    #Cmds

    @commands.command(aliases=['crossnnots'])
    async def tictac(self,ctx, player_2:discord.Member, sym_1="✖️",sym_2="⭕"):
        player_1 = ctx.author
        print(player_1, player_2)
        play = 1
        board = "```  1  |  2️  |  3️  \n-----|-----|-----\n  4️  |  5️  |  6️  \n-----|-----|-----\n  7️  |  8️  |  9️  ```"
        bmsg=await ctx.send(board)
        reactions = ('1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣')
        R = {'1️⃣':1,'2️⃣':2,'3️⃣':3,'4️⃣':4,'5️⃣':5,'6️⃣':6,'7️⃣':7,'8️⃣':8,'9️⃣':9}

        for n in reactions:
            await bmsg.add_reaction(n)

        for i in range(play, 9):
            print("turn" , i)
            def ch(reaction, user):
                if i%2 == 1:
                    print("1st player's turn")
                    turn = player_1
                else:
                    print("2nd player's turn")
                    turn = player_2
                print(reaction)
                print(user)
                return user==turn and str(reaction.emoji) in reactions
            react= await self.client.wait_for('reaction_add',check=ch)
            #print(f"here we have {react[1].user}")
            print(f"and this is {react[0].emoji}")
            p = R.get(react[0].emoji)
            if i%2 == 1:
                board= board.replace(str(p),f"{str(sym_1)}")
            else:
                board= board.replace(str(p),f"{str(sym_2)}")
            await bmsg.edit(content=board)
            await bmsg.clear_reaction(react[0].emoji)
            



def setup(client):
    client.add_cog(Games(client))
