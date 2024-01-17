import discord
from discord.ext import commands
import os
import asyncio
import config
import aiohttp

intents = discord.Intents.all()

def get_prefix(bot, message):
    prefixes = ['/', f'<@!{bot.user.id}> ']  # Adicione aqui os prefixos que você deseja
    return commands.when_mentioned_or(*prefixes)(bot, message)

client = commands.Bot(command_prefix=get_prefix, intents=intents)

# Função assíncrona para carregar cogs
async def load_cogs():
    for folder in os.listdir('./cogs'):
        if os.path.isdir(f'./cogs/{folder}'):
            for filename in os.listdir(f'./cogs/{folder}'):
                if filename.endswith('.py') and filename != '__init__.py':
                    cog_name = f'cogs.{folder}.{filename[:-3]}'
                    try:
                        setup_module = __import__(cog_name, fromlist=['setup'])
                        setup_function = setup_module.setup
                        await setup_function(client)
                        print(f'Cog adicionado com sucesso: {cog_name}')
                    except commands.ExtensionError as e:
                        print(f'Erro ao adicionar o cog {cog_name}: {e}')
                    except Exception as e:
                        print(f'Erro inesperado ao adicionar o cog {cog_name}: {e}')

# ...

async def setup_bot():
    await load_cogs()
    # Adicione a linha abaixo para carregar o cog de eventos de boas-vindas
    try:
        await client.start(config.TOKEN)
    finally:
        await client.close()
        await aiohttp.ClientSession.close()

asyncio.run(setup_bot())