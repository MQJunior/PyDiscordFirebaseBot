# ./cogs/parar.py
from discord.ext import commands

class PararCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='parar', help='Encerra a execução do bot (somente para o dono)')
    @commands.is_owner()
    async def parar_bot(self, ctx):
        print('Comando para PARAR o BOT ...')
        await ctx.send("Bot sendo desligado...")
        try:
            await self.bot.close()
        except:
            print('           Erro!        ')
        print('... BOT Finalizado!!! ')
        

async def setup(bot):
    cog = PararCog(bot)
    await bot.add_cog(cog)
