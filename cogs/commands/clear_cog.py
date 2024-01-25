# /cogs/clear_cog.py
from conf.languages import LANGUAGES
from discord.ext import commands
from utils.language_utils import *


class ClearCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='clear', help=get_language_value('command_clear_help'))
    async def clear_command(self, ctx):
        
        try:
            if ctx.author.guild_permissions.manage_messages:
                await ctx.channel.purge()
                await ctx.send('All messages cleared.')
            else:
                await ctx.send('You do not have the required permissions to use this command.')
        except Exception as e:
            await ctx.send(f'An error occurred: {e}')

async def setup(bot):
    cog = ClearCog(bot)
    await bot.add_cog(cog)
