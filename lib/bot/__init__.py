from glob import glob
from time import sleep

from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from discord.ext.commands import Bot as BotBase, cog
from discord.ext.commands import CommandNotFound
from discord.ext.commands.core import command
from discord.ext.commands.errors import CommandNotFound

from discord import Intents, client
from discord import Embed, File
import random, os



PREFIX = '+'

OWNER_IDS = [114719310819098629]
COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]

class bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        super().__init__(command_prefix=PREFIX, OWNER_IDS=OWNER_IDS, intents=Intents.all())
    
    def setup(self):
        for cog in COGS:
            self.load_extension(f"lib.cogs.{cog}")
            print(f"{cog} cog loaded")
        

    def run(self, version):
        self.VERSION = version

        print("Running setup...")
        self.setup()

        with open("./lib/bot/token", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()
        super().run(self.TOKEN, reconnect=True)


    async def on_connect(self):
            print('We have logged in as {0.user}'
            .format(bot))

    async def on_disconnect(self):
        print("Bot has disconnected.")

    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            await args[0].send("Something went wrong.")
            await self.stdout.send("An error occured.")
            raise

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            pass
        elif hasattr(exc, "original"):
            raise exc.original
        else:
            raise exc

    async def on_ready(self):
        if not self.ready:
            self.stdout = self.get_channel(856241227997642773)

            await self.stdout.send("Now online!")
            
            self.ready = True
            print('System Ready!')

            # await self.stdout.send("Ora ora ora!")
            # await self.stdout.send(file=File("data\jojo\image1.gif"))

        else:
            print("Bot Reconnected")

    async def on_message(self, message):
        pass


bot = bot()
