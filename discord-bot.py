import discord
import random
import urbandictionary as ud

client = discord.Client()
emb = discord.Embed()

TOKEN = 'Your Token Goes Here'

@client.event
async def on_ready():
    print("The Bot Is Ready")
    await client.change_presence(game=discord.Game(name="Type Halp for more Infor"))

images = ['https://imgur.com/puv8KUX', 'https://imgur.com/vtjx54A', 'https://imgur.com/0IXjXVN', 'https://imgur.com/yxY83CG', 'https://imgur.com/8d3ynyk' ,'https://imgur.com/BEEzk2v' , 'https://imgur.com/jtGQXpt' , 'https://imgur.com/fzCLu7j', 'https://imgur.com/gejV1Zt' , 'https://imgur.com/EGyAcOp', 'https://imgur.com/NLWTUMN']



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "hello":
        await message.channel.send("Hi")

    if message.content.lower() == "pong":
        await message.channel.send("I'm Alive, Chill with the Abuse!")

    if message.content.lower() == "hi":
        await message.channel.send("Hello " + message.author.mention)

    if message.content.lower() == "no u":
        await message.channel.send("no me " + message.author.mention)

    if message.content.lower().startswith("img"):
        emb.title = "Here is Random Image. Enjoy"
        emb.set_image(url = random.choice(images).replace("imgur.com", "i.imgur.com")+".jpg")
        await message.channel.send(embed=emb)

    if message.content.lower().startswith("halp"):
        emb.title = ('**__All available Commands__**')
        emb.description = ('Use Halp for Help\nHi and Hello to say hey\nImg to get a random image\nurb to search Urbandictionary. Urb for an random one, or add a term and search for it.')
        await message.channel.send(embed=emb)

    if message.content.lower()== "urb":
        r = ud.random()
        emb.title = r[0].word
        emb.description = r[0].definition
        await message.channel.send(embed=emb)

    if message.content.lower().startswith("urbkef"):
        f = ud.define('kef')
        emb.title = f[0].word
        emb.description = f[0].definition
        await message.channel.send(embed=emb)

    if message.content.lower().startswith("urb"):
        args = message.content.lower().split(" ", 1)
        d = ud.define(args[1])
        emb.title = d[0].word
        emb.description = d[0].definition
        await message.channel.send(embed=emb)


client.run(TOKEN)


