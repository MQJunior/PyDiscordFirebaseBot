# /cogs/language_cog.py

from discord.ext import commands
from conf.languages import LANGUAGES
from utils.language_utils import *

class LanguageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='setlanguage', aliases=['setlang'], help=get_language_value('command_help_set_language'))
    async def set_language_command(self, ctx, new_language: int):
        set_language(new_language, LANGUAGES)  # Adicione o segundo argumento
        
        tmp_msg = get_language_value('language_utils_set_language')
        tmp_msg_code = get_language_value('code')+' - '+get_language_value('name')
        await ctx.send(f"{tmp_msg} {tmp_msg_code}.")

    @commands.command(name='listlanguages', aliases=['listlangs'], help='List available bot languages')
    async def list_languages_command(self, ctx):
        lang = get_language
        language_list = "\n".join([f"{option} - {lang['name']} ({lang['code']})" for option, lang in LANGUAGES.items()])
        language_current = get_language_value('code')
        await ctx.send(f'({language_current}) '+get_language_value('command_list_languages')+f':\n{language_list}')
        
        
async def setup(bot):
    cog = LanguageCog(bot)
    await bot.add_cog(cog)
