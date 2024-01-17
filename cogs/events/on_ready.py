from discord.ext import commands

class OnReadyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot Online - {self.bot.user.name}')

async def setup(bot):
    cog = OnReadyCog(bot)
    await bot.add_cog(cog)
