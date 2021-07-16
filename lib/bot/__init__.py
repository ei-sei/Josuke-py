from glob import glob

from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from discord.ext.commands import Bot as BotBase, cog
from discord.ext.commands import CommandNotFound
from discord.ext.commands.core import command
from discord.ext.commands.errors import CommandNotFound

from discord import Intents, client
from discord import Embed, File

from ..db import db
import random, os



client  = commands.Bot(command_prefix = '.')

OWNER_IDS = [114719310819098629]
COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]

class Ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)

    def ready_up(self, cog):
        setattr(self, cog, True)
        #print(f"{cog} cog ready")
    
    def all_ready(self):
        return all([getattr(self, cog) for cog in COGS])

class bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.cogs_ready = Ready()
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        db.autosave(self.scheduler)
        super().__init__(command_prefix=PREFIX, OWNER_IDS=OWNER_IDS, intents=Intents.all())
    
    def setup(self):
        for cog in COGS:
            print(f"{cog} cog loaded")


    def run(self, version):
        self.VERSION = version

        print("Running setup...")
        self.setup()

        with open("./lib/bot/token", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()
        #print("Starting up bot...")
        super().run(self.TOKEN, reconnect=True)


    async def on_connect(self):
        print("Systems ready!")

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
            self.scheduler.add_job(self.rules_reminder, CronTrigger(day_of_week=0, hour=12, minute=0, second=0))
            self.scheduler.start()

            # self.update_db()
            
            # embed = Embed(title="Now online!", description="Shakeey",
            # colour=0xFF0000, )
            # fields = [("Name", "Value", True),
            # ("Another field", "This field is next to the other one.", True),
            # ("A non-inline field", "This field will appear on its own row", False)]
            # for name, value, inline in fields:
            #     embed.add_field(name=name, value=value, inline=inline)
            # await channel.send(embed=embed)


            # while not self.cogs_ready.all_ready():
            #     await sleep(0.5)

            await self.stdout.send("Now online!")
            
            self.ready = True
            print('We have logged in as {0.user}'
            .format(bot))

            # await self.stdout.send("Ora ora ora!")
            # await self.stdout.send(file=File("data\jojo\image1.gif"))

        else:
            print("Bot Reconnected")

    async def on_message(self, message):
        pass


bot = bot()
