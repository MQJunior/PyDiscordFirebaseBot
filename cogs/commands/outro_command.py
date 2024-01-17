from discord.ext import commands

class OutroCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='outro', help='Test outro command example')
    async def outro_command(self, ctx):
        await ctx.send('Outro Comando Executado!')

async def setup(bot):
    cog = OutroCog(bot)
    await bot.add_cog(cog)
