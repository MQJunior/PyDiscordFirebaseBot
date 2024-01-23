import discord
from discord.ext import commands
import os
import asyncio
import conf.config as config
import aiohttp
import logging

from conf.languages import LANGUAGES
from conf import logger_config
from conf.lang_config import *
from utils.language_utils import set_language, get_language


intents = discord.Intents.all()

def get_prefix(bot, message):
    prefixes = ['/', f'<@!{bot.user.id}> ']  # Adicione aqui os prefixos que você deseja
    return commands.when_mentioned_or(*prefixes)(bot, message)

class CustomHelpCommand(commands.HelpCommand):
    def __init__(self, language_options):
        super().__init__()
        self.language_options = language_options
    
    async def send_bot_help(self, mapping):
        lang = get_language()  # Obtendo as mensagens no idioma correto

        # Adicionando a seção de idiomas
        language_list = "\n".join([f"{option} - {lang['name']} ({lang['code']})" for option, lang in self.language_options.items()])
        language_section = f"**{get_language_value('command_help_set_language')}**: `/listlanguages` - {get_language_value('command_help_set_language')}\n{language_list}\n\n"

        embed = discord.Embed(
            title=get_language_value('help_title'),
            description=f"{language_section}{get_language_value('help_description')}",
            color=discord.Color.blue()
        )

        for cog, commands in mapping.items():
            if cog:
                for command in commands:
                    command_name = '/'+command.name
                    command_help = command.help
                    embed.add_field(name=command_name, value=command_help, inline=False)
            else:
                for command in commands:
                    command_name = '/'+command.name
                    command_help = command.help
                    embed.add_field(name=command_name, value=command_help, inline=False)

        await self.get_destination().send(embed=embed)

client = commands.Bot(command_prefix=get_prefix, intents=intents, help_command=CustomHelpCommand(LANGUAGES))


async def load_cogs():
    lang = get_language()
    for folder in os.listdir('./cogs'):
        if os.path.isdir(f'./cogs/{folder}'):
            for filename in os.listdir(f'./cogs/{folder}'):
                if filename.endswith('.py') and filename != '__init__.py':
                    cog_name = f'cogs.{folder}.{filename[:-3]}'
                    try:
                        setup_module = __import__(cog_name, fromlist=['setup'])
                        setup_function = setup_module.setup
                        await setup_function(client)
                        logging.info(get_language_value('load_cogs_sucess') + cog_name)
                    except commands.ExtensionError as e:
                        tmp_msg = get_language_value('load_cogs_error_add')
                        logging.error(f'{tmp_msg} - {cog_name}: {e}')
                    except Exception as e:
                        tmp_msg = get_language_value('load_cogs_error')
                        logging.error(f'{tmp_msg} {cog_name}: {e}')

async def setup_bot():
    await load_cogs()
    try:
        await client.start(config.TOKEN)
    except Exception as e:
        logging.error(f"Erro ao iniciar o Bot: {e}")
    finally:
        try:
            await client.close()
        except Exception as e:
            logging.error(f'Erro ao fechar o bot: {e}')
        try:
            await aiohttp.ClientSession.close()
        except Exception as e:
            logging.error(f'Erro ao fechar a sessão aiohttp: {e}')

if __name__ == "__main__":
    asyncio.run(setup_bot())
