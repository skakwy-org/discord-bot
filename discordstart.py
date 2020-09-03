import discord
from discord.utils import get
client = discord.Client()



@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    #get the author of the message
    author = message.author.mention

    if message.author == client.user:
        return

    #check what the author wrote and if the message is hey response with hey and a mention
    if message.content.startswith('hey'):
        await message.channel.send('hey ' + author)
#Enter you bot token here. To get it go on the bot and on the left side on bot and press copy and now you copied the bot token should look something like this NzUxMDEwNjQ1NzAwMjQ3NTYy.X1C3Kw.AGbbonEkde6ugeFTkWatxMtRnq
client.run('token')
