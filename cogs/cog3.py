import discord
from discord.ext import commands
#import datetime
import random
import string

class Games(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Events

    #Cmds

    @commands.command(aliases=['xno'])
    async def tictac(self,ctx, player_2:discord.Member, sym_1="✖️",sym_2="⭕"):
        if player_2.bot:
            await ctx.send("Can't play with a bot")
            if ctx.author.id!=444806806682730496:
              return
        player_1 = ctx.author
        print(player_1, player_2)
        #play = 1
        board = "```  1  |  2️  |  3️  \n-----|-----|-----\n  4️  |  5️  |  6️  \n-----|-----|-----\n  7️  |  8️  |  9️  ```"
        bmsg=await ctx.send(board)
        reactions = ('1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣')
        R = {'1️⃣':1,'2️⃣':2,'3️⃣':3,'4️⃣':4,'5️⃣':5,'6️⃣':6,'7️⃣':7,'8️⃣':8,'9️⃣':9}

        for n in reactions:
            await bmsg.add_reaction(n)

        for i in range(9):
            print("turn" , i)
            def ch(reaction, user):
                if i%2 != 1:
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
            
    @commands.command() # how about make it edit the 1st msgs every letter
    async def hangman(self,ctx):
        """You've 5 tries to guess a letters of a random word (please send 1 letter at a time)""" # # word count in english2.txt is 65194 words!
        word=random.choice(open("english2.txt","r").read().split())
        #region initialization
        win = False
        strikes = [] # can do win=False if strikes==5
        guesses = []
        display_word = len(word)*['- '] 
        print("\nLet's play HANGMAN!\n")
        print(word,"\n",display_word,'\n')
        await ctx.send("Let's play HANGMAN! Can you guess in 5 strikes?")
        await ctx.send(content=("".join(display_word)+"\n."))
        #endregion
        #region game loop
        while (win == False) and (len(strikes) < 5):
          #  letter = raw_input("Guess a letter! ").lower()
          #  define bmsg
            def ch(message):
              return message.author.bot==False
            msg= await self.client.wait_for('message',check=ch)
            #print(msg)
            letter=msg.content.lower()
            print(letter)
            await ctx.trigger_typing()

            if not letter in string.ascii_lowercase or letter=='':
                #await ctx.send("not a valid guess, please try again")
                continue

            if letter in guesses:
                await msg.reply('You already guessed that one, please try again.')
            else:
                guesses += [letter]
                if letter in word:
                    print("\nCorrect Guess!",letter)
                    await msg.reply(f"Yes!   **{letter}**")
                    for x in range(0, len(word)):
                        if letter == word[x]:
                          display_word[x] = word[x]
                else:
                    strikes += [letter]
                    print("\nIncorrect Guess.")
                    await msg.reply("wrong guess...")

            await ctx.send(embed=discord.Embed(title="The mystery word so far:",description= "".join(display_word)))
            await ctx.send(("Already guessed letters: ", guesses))
            await ctx.send(("Strikes remaining: " + str(5-len(strikes)))) #send pic of hangman
            if display_word == list(word):
                win = True
            #print(win)
        #endregion

        if win == True:
            await msg.reply("Hats off to you! You win!")
        else:
            hang="```\n\t|\n\to\n  --|--\n   /\```"
            await msg.reply(f"You lost this time.\nCan't win 'em all.\n{hang}")
        print("The word was '", ''.join(word) , "'")
        await ctx.send("The word is '"+''.join(word)+"'")

        await ctx.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')



def setup(client):
    client.add_cog(Games(client))