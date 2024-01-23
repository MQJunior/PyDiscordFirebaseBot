import discord
from discord.ext import commands
from datetime import datetime

async def enviar_log(bot, canal_id, mensagem):
    try:
        canal = bot.get_channel(canal_id)
    except Exception as e:
        print(f'Erro ao acessar o canal de LOGs: {e}')

    if canal:
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mensagem_com_data = f"{data_hora} - {mensagem}"
        await canal.send(mensagem_com_data)
        print(f"Mensagem enviada para o canal de logs.")
    else:
        print("Canal de logs não encontrado. Certifique-se de que o bot tem acesso ao canal.")


async def obter_lista_canais(servidor):
    return [canal for canal in servidor.channels if isinstance(canal, discord.TextChannel)]
