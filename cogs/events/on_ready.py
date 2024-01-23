from discord.ext import commands
from utils.firebase_utils import is_channel_log_defined
from utils.discord_utils import enviar_log

class OnReadyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        
        channel_log_defined = is_channel_log_defined()

        if channel_log_defined:
            print("Canal de logs definido no Firebase.")
        else:
            print("Canal de logs não definido no Firebase.")
        print(f'Bot Online - {self.bot.user.name}')
        
        await enviar_log(self.bot, 1198099611529777204, 'Bot Logado')
        

async def setup(bot):
    cog = OnReadyCog(bot)
    await bot.add_cog(cog)
