import discord

class mybot(discord.Client):
    async def on_ready(self):
        print("Reborn: {0}".format(self.user))

    async def on_message(self, msg):
        if msg.author == self.user:
            return

        if msg.content == 'ping':
            await msg.channel.send(f"PONG! {round(client.latency * 1000)}ms")
        
        if {msg.content == "Hi"} | {msg.content == "Hey"} | {msg.content == 'Hello'}:
            await msg.channel.send("Heyo~")


client = mybot()
client.run(Disc_Token)
