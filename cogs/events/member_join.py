import discord
from discord.ext import commands

class MemberJoinCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'Novo Membro adicionado...{member.name}')
        
        # Canal de boas-vindas (substitua 'ID_DO_CANAL' pelo ID real do canal)
        welcome_channel = self.bot.get_channel('ID_DO_CANAL')
        
        if welcome_channel:
            print(f"Canal de boas-vindas encontrado: {welcome_channel.name} ({welcome_channel.id})")
            
            embed = discord.Embed(
                title=f"Bem-vindo(a) ao servidor, {member.name}!",
                description=f"Esperamos que você aproveite o tempo por aqui.",
                color=discord.Color.green().value  # Cor verde (você pode personalizar)
            )
            embed.set_thumbnail(url=member.avatar_url)
            print("Embed Gerado... Enviando Embed... ")
            await welcome_channel.send(embed=embed)
            print(f'Mensagem de Boas Vindas exibida ao Membro: {member.name}')
        else:
            print(f"Canal de boas-vindas não encontrado para o membro {member.name} ({member.id}).")
            print("Certifique-se de que o ID do canal está correto e que o bot tem permissões para enviar mensagens no canal.")

async def setup(bot):
    cog = MemberJoinCog(bot)
    await bot.add_cog(cog)
