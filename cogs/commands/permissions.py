from discord.ext import commands

class PermissionsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='permissions', help='Mostra as permissões do Bot no Canal')
    async def get_bot_permissions(self, ctx):
        print('Executando Comando permissions ')
        # Verifica se o autor do comando é um administrador do servidor
        if ctx.author.guild_permissions.administrator:
            # Obtém as permissões do bot no canal atual
            print("Permissao: ")
            bot_permissions = ctx.channel.permissions_for(ctx.guild.me)

            print(" ... Administrador")
            # Cria uma lista de permissões concedidas
            allowed_permissions = [perm for perm, value in bot_permissions if value]
            
            # Envia a lista de permissões no canal
            await ctx.send(f"Permissões concedidas para o bot neste canal: {', '.join(allowed_permissions)}")
            print(f"Permissões concedidas para o bot neste canal: {', '.join(allowed_permissions)}")
        else:
            print('Membro')
            await ctx.send("Você não tem permissão para usar este comando.")
            print("Você não tem permissão para usar este comando.")

async def setup(bot):
    cog = PermissionsCog(bot)
    await bot.add_cog(cog)