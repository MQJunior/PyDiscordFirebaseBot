import discord
from discord.ext import commands
from discord.ui import Button, View

class BotaoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='botao')  # Nome do seu comando
    async def seubotao_command(self, ctx):
        # Criar um botão
        button = Button(style=discord.ButtonStyle.primary, label="Seu Botão")

        # Adicionar a função de callback ao botão
        async def button_callback(interaction: discord.Interaction):
            await interaction.response.send_message("Você pressionou o botão!")

            # Executar o comando desejado
            ctx = await self.bot.get_context(interaction.message)
            await self.bot.invoke(ctx)

        button.callback = button_callback

        # Adicionar o botão a uma view
        view = View()
        view.add_item(button)

        # Enviar uma mensagem com o botão
        message = await ctx.send("Mensagem do Seu Bot!", view=view)
        
async def setup(bot):
    cog = BotaoCog(bot)
    await bot.add_cog(cog)
