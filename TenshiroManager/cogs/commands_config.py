# cogs/commands_config.py
import discord
from discord import app_commands
from discord.ext import commands
from utils.io_utils import load, save

class CommandsConfig(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="addcommand", description="Ajoute une commande dans une catégorie du help.")
    @app_commands.describe(categorie="Catégorie de la commande", commande="Commande à ajouter", description="Description de la commande")
    async def addcommand(self, interaction: discord.Interaction, categorie: str, commande: str, description: str):
        config = load("config.json")
        if str(interaction.user.id) not in config["system"]:
            await interaction.response.send_message("❌ Tu n’as pas la permission d’ajouter une commande.", ephemeral=True)
            return

        if categorie not in config:
            config[categorie] = []

        config[categorie].append({"commande": commande, "description": description})
        save(config, "config.json")
        await interaction.response.send_message(f"✅ Commande `{commande}` ajoutée à la catégorie **{categorie}**.")

    @app_commands.command(name="removecommand", description="Supprime une commande d'une catégorie.")
    @app_commands.describe(categorie="Catégorie de la commande", commande="Commande à supprimer")
    async def removecommand(self, interaction: discord.Interaction, categorie: str, commande: str):
        config = load("config.json")
        if str(interaction.user.id) not in config["system"]:
            await interaction.response.send_message("❌ Tu n’as pas la permission de retirer une commande.", ephemeral=True)
            return

        if categorie in config:
            before = len(config[categorie])
            config[categorie] = [cmd for cmd in config[categorie] if cmd["commande"] != commande]
            save(config, "config.json")
            if before == len(config[categorie]):
                await interaction.response.send_message("❌ Commande non trouvée.")
            else:
                await interaction.response.send_message(f"✅ Commande `{commande}` supprimée de la catégorie **{categorie}**.")
        else:
            await interaction.response.send_message("❌ Catégorie introuvable.")


async def setup(bot):
    await bot.add_cog(CommandsConfig(bot))
