# cogs/clear.py
import discord
from discord.ext import commands
from utils.io_utils import load, save

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self, ctx, arg=None, option=None):
        config = load("config.json")

        if arg == "limit":
            if str(ctx.author.id) not in config["system"]:
                await ctx.send(embed=discord.Embed(description="Vous n'avez pas l'autorisation de définir la limite."))
                return

            if not option or not option.isdigit():
                await ctx.send(embed=discord.Embed(description="Veuillez spécifier une limite numérique."))
                return

            config["max_clear"] = int(option)
            save(config, "config.json")
            await ctx.send(embed=discord.Embed(description=f"Limite de suppression fixée à {option} messages."))
            return

        if arg and arg.isdigit():
            if str(ctx.author.id) not in config["system"]:
                await ctx.send(embed=discord.Embed(description="Vous n'avez pas l'autorisation d'utiliser cette commande."))
                return

            limit = config.get("max_clear", 100)
            if int(arg) > int(limit):
                await ctx.send(embed=discord.Embed(description=f"Vous pouvez supprimer au maximum {limit} messages."))
                return

            deleted = await ctx.channel.purge(limit=int(arg))
            await ctx.send(embed=discord.Embed(description=f"🧹 {len(deleted)} messages supprimés."), delete_after=5)


async def setup(bot):
    await bot.add_cog(Clear(bot))
