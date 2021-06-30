from discord import Intents
from apscheduler.schedulers.asyncio import  AsyncIOScheduler
from discord.ext.commands import Bot as BotBase

PREFIX = "+"
OWNER_IDS = [114719310819098629]

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler  =AsyncIOScheduler()

        super().__init__(
            command_prefix=PREFIX, 
            OWNER_IDS=OWNER_IDS,
            intents = Intents.all(),
            )
    
    def run(self, version):
        self.VERSION = version

        with open("./lib/bot/token", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()
        
        print("Starting up bot...")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("Systems ready!")

    async def on_disconnect(self):
        print("Bot has disconnected")
    
    async def on_ready(self):
        if not self.ready:
            self.ready = True
            print("Bot ready")
            
        
        else:
            print("Bot Reconnected")


    async def on_message(self, message):
        pass

bot = Bot()