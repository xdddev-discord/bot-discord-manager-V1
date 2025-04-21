# cogs/privacy.py
import discord
from discord.ext import commands
from utils.io_utils import load, save

class Privacy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pv(self, ctx):
        config = load("config.json")
        author_id = str(ctx.author.id)
        channel_id = str(ctx.channel.id)

        if author_id in config["system"] or author_id in config["owner"]:
            if channel_id in config["pv"]:
                await ctx.send(embed=discord.Embed(description="Ce channel est déjà privé !"))
                return

            config["pv"].append(channel_id)
            save(config, "config.json")
            await ctx.channel.set_permissions(ctx.guild.default_role, view_channel=False)
            await ctx.send(embed=discord.Embed(description="Ce channel a bien été rendu privé !"))
        else:
            await ctx.send(embed=discord.Embed(description="Vous n'avez pas la permission de rendre ce channel privé."))

    @commands.command()
    async def unpv(self, ctx):
        config = load("config.json")
        author_id = str(ctx.author.id)
        channel_id = str(ctx.channel.id)

        if author_id in config["system"] or author_id in config["owner"]:
            if channel_id not in config["pv"]:
                await ctx.send(embed=discord.Embed(description="Ce channel n'est pas privé !"))
                return

            config["pv"].remove(channel_id)
            save(config, "config.json")
            await ctx.channel.set_permissions(ctx.guild.default_role, view_channel=True)
            await ctx.send(embed=discord.Embed(description="Ce channel a bien été rendu public !"))
        else:
            await ctx.send(embed=discord.Embed(description="Vous n'avez pas la permission de rendre ce channel public."))


async def setup(bot):
    await bot.add_cog(Privacy(bot))
