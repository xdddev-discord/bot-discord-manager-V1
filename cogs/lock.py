# cogs/lock.py
import discord
from discord.ext import commands
from utils.io_utils import load, save

class Lock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lock(self, ctx):
        config = load("config.json")
        author_id = str(ctx.author.id)

        if author_id in config.get("system", []) or author_id in config.get("owner", []) or author_id in config.get("trust", []):
            if "lock" not in config:
                config["lock"] = []

            channel_id = str(ctx.channel.id)
            if channel_id in config["lock"]:
                await ctx.send(embed=discord.Embed(description="🔒 Ce salon est déjà lock."))
                return

            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False, add_reactions=False)
            config["lock"].append(channel_id)
            save(config, "config.json")
            await ctx.send(embed=discord.Embed(description=f"🔒 Le salon {ctx.channel.mention} a été lock."))
        else:
            await ctx.send("❌ Vous n'avez pas la permission d'utiliser cette commande.")

    @commands.command()
    async def unlock(self, ctx):
        config = load("config.json")
        author_id = str(ctx.author.id)

        if author_id in config.get("system", []) or author_id in config.get("owner", []) or author_id in config.get("trust", []):
            if "lock" not in config:
                config["lock"] = []

            channel_id = str(ctx.channel.id)
            if channel_id not in config["lock"]:
                await ctx.send(embed=discord.Embed(description="🔒 Ce salon n'est pas lock."))
                return

            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True, add_reactions=True)
            config["lock"].remove(channel_id)
            save(config, "config.json")
            await ctx.send(embed=discord.Embed(description=f"🔓 Le salon {ctx.channel.mention} a été unlock."))
        else:
            await ctx.send("❌ Vous n'avez pas la permission d'utiliser cette commande.")


async def setup(bot):
    await bot.add_cog(Lock(bot))
