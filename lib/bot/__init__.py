from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.cron.fields import DayOfWeekField
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from discord.ext.commands import Bot as BotBase
from discord.ext.commands import CommandNotFound
from discord.ext.commands.errors import CommandNotFound

from discord import Intents
from discord import Embed, File

from ..db import db
import random, os



PREFIX = "+"
OWNER_IDS = [114719310819098629]


class client(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        db.autosave(self.scheduler)
        super().__init__(
            command_prefix=PREFIX,
            OWNER_IDS=OWNER_IDS,
            intents=Intents.all(),
        )

    def run(self, version):
        self.VERSION = version

        with open("./lib/bot/token", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("Starting up bot...")
        super().run(self.TOKEN, reconnect=True)

    async def print_message(self):
        channel = self.get_channel(856241227997642773)
        await channel.send("I am a timed notification.")

    async def on_connect(self):
        print("Systems ready!")

    async def on_disconnect(self):
        print("Bot has disconnected.")

    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            await args[0].send("Something went wrong.")

            channel = self.get_channel(856241227997642773)
            await channel.send("An error occured.")
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
            self.ready = True
            # self.scheduler.add_job(self.print_message, CronTrigger(DayOfWeekField == 0, hour=0))
            # self.scheduler.start()
            
            channel = self.get_channel(856241227997642773)
            await channel.send("Ora ora ora!")

            # embed = Embed(title="Now online!", description="Shakeey",
            # colour=0xFF0000, )
            # fields = [("Name", "Value", True),
            # ("Another field", "This field is next to the other one.", True),
            # ("A non-inline field", "This field will appear on its own row", False)]
            # for name, value, inline in fields:
            #     embed.add_field(name=name, value=value, inline=inline)
            # await channel.send(embed=embed)

            print("Bot ready.")
            await channel.send(file=File("data\jojo\image1.gif"))
        else:
            print("Bot Reconnected")

    async def on_message(self, message):
        pass


client = client()
