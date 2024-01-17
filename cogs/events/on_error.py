import discord
from discord.ext import commands

class OnErrorCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_error(self, event, *args, **kwargs):
        # Aqui você pode personalizar como deseja lidar com os erros
        # Este exemplo apenas imprime o erro no console
        print(f'Error during {event}:')
        for arg in args:
            print(arg)
        print(kwargs)

async def setup(bot):
    cog = OnErrorCog(bot)
    await bot.add_cog(cog)
