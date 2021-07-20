import os
from discord import client
from dotenv.main import load_dotenv
from lib.bot import bot

VERSION = "0.0.5"

#bot.run(VERSION)
load_dotenv()
client.run(os.environ.get("SECRET_KEY"))