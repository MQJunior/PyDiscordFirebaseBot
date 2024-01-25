from discord.ext import commands

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test', help='Test command example')
    async def test_command(self, ctx):
        await ctx.send('Test command executed!')

async def setup(bot):
    cog = TestCog(bot)
    await bot.add_cog(cog)
