import discord
from discord.ext import commands

class FormularioCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='formulario')
    async def enviar_formulario(self, ctx):
        # Perguntas do formulário
        perguntas = [
            "Qual é o seu nome?",
            "Qual é a sua idade?",
            "O que você acha do bot?",
        ]

        # Inicializa as respostas
        respostas = []

        # Envia as perguntas e aguarda as respostas do usuário
        for pergunta in perguntas:
            await ctx.send(pergunta)
            resposta = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author)
            respostas.append(resposta.content)

        # Exibe ou envia as respostas
        resposta_final = "\n".join(f"{pergunta}: {resposta}" for pergunta, resposta in zip(perguntas, respostas))
        await ctx.send(f"Formulário concluído!\n{resposta_final}")

async def setup(bot):
    cog = FormularioCog(bot)
    await bot.add_cog(cog)
