# cogs/vcpv.py
import discord
from discord.ext import commands
from utils.io_utils import load, save

class Vcpv(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def vcpv(self, ctx, arg: str, id: discord.Member = None):
        config = load("config.json")
        fichier = "config.json"

        if arg == "create":
            if not id:
                await ctx.send(embed=discord.Embed(description="Utilisateur introuvable"))
                return

            if str(ctx.author.id) not in config["system"]:
                await ctx.send(embed=discord.Embed(description="Vous n'avez pas les permissions requises."))
                return

            category = ctx.guild.get_channel(config.get("vcpv_catégorie"))
            salon = await ctx.guild.create_voice_channel(name=f"{id.name} - voc perso", category=category)
            await salon.set_permissions(ctx.guild.default_role, view_channel=False)
            await salon.set_permissions(id, view_channel=True, connect=True, speak=True, stream=True, mute_members=True, deafen_members=True)

            config["vcpv"][str(salon.id)] = str(id.id)
            save(config, fichier)

            await ctx.send(f"Salon vocal perso créé pour {id.name}.")

        elif arg == "delete":
            if str(ctx.author.id) not in config["system"]:
                await ctx.send(embed=discord.Embed(description="Vous n'avez pas les permissions requises."))
                return

            if not id:
                await ctx.send(embed=discord.Embed(description="Utilisateur introuvable"))
                return

            salon_id = next((sid for sid, uid in config["vcpv"].items() if uid == str(id.id)), None)
            if not salon_id:
                await ctx.send(f"Aucun salon trouvé pour {id.mention}")
                return

            salon = ctx.guild.get_channel(int(salon_id))
            if salon:
                await salon.delete()

            del config["vcpv"][salon_id]
            save(config, fichier)
            await ctx.send(f"Salon vocal supprimé pour {id.mention}.")

        elif arg == "list":
            vcpv_dict = config.get("vcpv", {})
            if not vcpv_dict:
                await ctx.send("Aucun salon enregistré.")
                return

            embed = discord.Embed(title="📋 Liste des vocaux persos")
            for salon_id, user_id in vcpv_dict.items():
                member = ctx.guild.get_member(int(user_id))
                username = member.name if member else f"Utilisateur inconnu ({user_id})"
                embed.add_field(name=f"Salon ID : {salon_id}", value=f"👤 {username}", inline=False)

            await ctx.send(embed=embed)

        elif arg == "add":
            if not id:
                await ctx.send("Veuillez mentionner un membre à ajouter.")
                return

            salon_id = next((sid for sid, uid in config["vcpv"].items() if uid == str(ctx.author.id)), None)
            if not salon_id:
                await ctx.send("Vous ne possédez pas de salon vocal personnel.")
                return

            salon = ctx.guild.get_channel(int(salon_id))
            await salon.set_permissions(id, connect=True, view_channel=True, speak=True)
            await ctx.send(f"{id.mention} a maintenant accès au salon.")

        elif arg == "remove":
            if not id:
                await ctx.send("Veuillez mentionner un membre à retirer.")
                return

            salon_id = next((sid for sid, uid in config["vcpv"].items() if uid == str(ctx.author.id)), None)
            if not salon_id:
                await ctx.send("Vous ne possédez pas de salon vocal personnel.")
                return

            salon = ctx.guild.get_channel(int(salon_id))
            await salon.set_permissions(id, overwrite=None)
            await ctx.send(f"{id.mention} n’a plus accès au salon.")


async def setup(bot):
    await bot.add_cog(Vcpv(bot))
