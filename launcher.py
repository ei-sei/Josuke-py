from lib.bot import bot
import os

VERSION = "0.0.1"

bot.run(os.environ.get("SECRET_KEY"))
