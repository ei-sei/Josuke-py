import discord
import os
import requests
import json
import random

import os
from dotenv import load_dotenv

load_dotenv()

#Stores bot within client variable
client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "miserable", "depressing"]
starter_encouragements = ["Cheer up!", "Hang in there!", "You are a great person / bot!"]

#Quote functionality
def get_quote():
    response = requests.get("Https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)



#Indicating functionality
@client.event
async def on_ready():
    print('We have logged in as {0.user}'
    .format(client))


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

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))


client.run(os.environ.get("SECRET_KEY"))
