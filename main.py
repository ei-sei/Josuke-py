import discord
from discord import colour
from discord import embeds
import requests
import json
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import DMChannel

load_dotenv()

#client = discord.Client()
#intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.')


#Status
@client.event
async def on_ready():
    print('We have logged in as {0.user}'
    .format(client))


#Join
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

#get a quote
def get_quote():
    response = requests.get("Https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)


#specific keyword prompt
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content
    
    if msg.startswith('quote'):
        quote = get_quote()
        await message.channel.send(quote)
    
    if msg.startswith('test'):
        await message.channel.send('I am fully functional!')
        

#DM
@client.command(name='dmsend', pass_context=True)
async def dmsend(ctx):
    user = await client.fetch_user("228950942337335298")
    await DMChannel.send(user, "stop be gay!")

'''
#embeds
@client.command()
async def displayembed():
    embed = discord.Embed(
        title = 'Title',
        description = 'The description',
        colour = discord.colour.blue()
    )

    embed.set_footer(text='The footer')
    embed.set_image(url='https://cdn.discordapp.com/attachments/784906587567292446/856873777937907742/Jojolion_.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/784906587567292446/856873777937907742/Jojolion_.png')
    embed.set_author(name='Author Name', 
    icon_url='https://cdn.discordapp.com/attachments/784906587567292446/856873777937907742/Jojolion_.png')
    embed.add_field(name='Field', value='Field value', inline=False)
    embed.add_field(name='Field', value='Field value', inline=True)
    embed.add_field(name='Field', value='Field value', inline=True)

    await client.say(embed=embed)
'''

client.run(os.environ.get("SECRET_KEY"))
