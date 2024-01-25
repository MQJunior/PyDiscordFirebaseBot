from discord.ext import commands

class ExemploCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    cog = ExemploCog(bot)
    await bot.add_cog(cog)
