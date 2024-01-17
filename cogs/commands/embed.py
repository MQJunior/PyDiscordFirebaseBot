from discord.ext import commands
import discord

class EmbedCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='embed')
    async def show_embed_example(self, ctx):
        print('Executando Comando Embed ... ')
        # Cria uma instância de Embed
        embed = discord.Embed(
            title="Exemplo de Embed",
            description="Este é um exemplo de embed utilizando Discord.py",
            color=discord.Color.blue().value  # Corrigido aqui
        )
        print('... Embed Criado ...')
        # Adiciona campos ao embed
        embed.add_field(name="Campo 1", value="Valor 1", inline=True)
        embed.add_field(name="Campo 2", value="Valor 2", inline=True)
        embed.add_field(name="Campo 3", value="Valor 3", inline=False)

        # Adiciona um rodapé ao embed
        embed.set_footer(text="Este é o rodapé do embed")

        # Envia o embed no canal
        await ctx.send(embed=embed)
        print('... Embed Enviado !!!')

async def setup(bot):
    cog = EmbedCog(bot)
    await bot.add_cog(cog)
