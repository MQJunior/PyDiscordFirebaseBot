from discord.ext import commands
from utils.discord_utils import obter_lista_canais
from utils.firebase_utils import set_channel_log_id

class ConfigCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='definircanaldelogs', help='Define o canal de Logs do Bot')
    async def definir_canal_de_logs(self, ctx):
        # Obtém a lista de canais do servidor
        canais_disponiveis = await obter_lista_canais(ctx.guild)

        if not canais_disponiveis:
            await ctx.send("Não há canais de texto disponíveis neste servidor.")
            return

        # Monta as opções do formulário com os nomes dos canais
        opcoes_formulario = {str(i + 1): canal.name for i, canal in enumerate(canais_disponiveis)}

        # Pergunta ao usuário qual canal ele quer usar
        mensagem_formulario = "Selecione o número do canal que você deseja definir como canal de logs:"
        for opcao, nome_canal in opcoes_formulario.items():
            mensagem_formulario += f"\n{opcao}. {nome_canal}"

        await ctx.send(mensagem_formulario)

        # Função para verificar a resposta do usuário
        def verificar_resposta(mensagem):
            return (
                mensagem.author == ctx.author
                and mensagem.channel == ctx.channel
                and mensagem.content.isdigit()
                and 1 <= int(mensagem.content) <= len(canais_disponiveis)
            )

        try:
            resposta = await self.bot.wait_for('message', check=verificar_resposta, timeout=30)
            indice_canal_escolhido = int(resposta.content) - 1
            canal_escolhido = canais_disponiveis[indice_canal_escolhido]

            # Salva o canal de logs no Firebase
            set_channel_log_id(canal_escolhido.id)
            await ctx.send(f"Canal de logs definido como {canal_escolhido.mention}.")
        except TimeoutError:
            await ctx.send("Tempo esgotado. O comando foi cancelado.")
        except Exception as e:
            print(f"Erro ao definir o canal de logs: {e}")
            await ctx.send("Ocorreu um erro ao definir o canal de logs. Tente novamente mais tarde.")

async def setup(bot):
    cog = ConfigCog(bot)
    await bot.add_cog(cog)