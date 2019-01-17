import discord
import random
import urbandictionary as ud

client = discord.Client()

TOKEN = 'Your Token Goes Here'

@client.event
async def on_ready():
    print("The Bot Is Ready")
    await client.change_presence(game=discord.Game(name="Type Halp for more Info"))

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

    if message.content.lower() == "img":
        emb1 = discord.Embed()
        emb1.title = "Here is Random Image. Enjoy"
        emb1.set_image(url = random.choice(images).replace("imgur.com", "i.imgur.com")+".jpg")
        await message.channel.send(embed=emb1)

    if message.content.lower().startswith("halp"):
        emb2 = discord.Embed()
        emb2.title = ('**__All available Commands__**')
        emb2.description = ('Use Halp for Help\nHi and Hello to say hey\nImg to get a random image\nurb to search Urbandictionary. Urb for an random one, or add a term and search for it.')
        await message.channel.send(embed=emb2)

    if message.content.lower().startswith("rand"):
        emb3 = discord.Embed()
        r = ud.random()
        emb3.title = r[0].word
        emb3.description = r[0].definition
        await message.channel.send(embed=emb3)


    if message.content.lower().startswith("urbkef"):
        emb4 = discord.Embed()
        f = ud.define('kef')
        emb4.title = f[0].word
        emb4.description = f[0].definition
        await message.channel.send(embed=emb4)

    if message.content.lower().startswith("urb"):
        emb5 = discord.Embed()
        args = message.content.lower().split(" ", 1)
        d = ud.define(args[1])
        emb5.title = d[0].word
        emb5.description = d[0].definition
        await message.channel.send(embed=emb5)


client.run(TOKEN)
