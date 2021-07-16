from discord.ext.commands import Cog

class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("fun")
            
        await self.bot.stdout.send("Cogs are in motion")
    
    @Cog.event()
    async def on_message(message):

        msg = message.content

        if msg.startswith('test'):
            await message.channel.send('I am fully functional!')


def setup(bot):
    bot.add_cog(Fun(bot))

#cogs sucks