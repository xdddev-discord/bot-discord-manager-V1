# cogs/help.py
import discord
from discord.ext import commands
from discord.ui import Button, View
from utils.io_utils import load

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        config = load("config.json")
        embeds = []
        categories = list(config.items())

        for category, commands_list in categories:
            if isinstance(commands_list, list) and commands_list and isinstance(commands_list[0], dict):
                value = ""
                for cmd in commands_list:
                    value += f"`{cmd['commande']}`\n→ {cmd['description']}\n\n"

                embed = discord.Embed(title=f"Help - **{category}**", color=discord.Color.from_rgb(5, 5, 5))
                embed.add_field(name=f"", value=value, inline=False)
                embeds.append(embed)

        message = await ctx.send(embed=embeds[0])
        if len(embeds) > 1:
            current_page = 0
            prev_button = Button(label="⬅️ Précédent", style=discord.ButtonStyle.secondary)
            next_button = Button(label="Suivant ➡️", style=discord.ButtonStyle.secondary)

            async def prev_button_callback(interaction: discord.Interaction):
                nonlocal current_page
                current_page = (current_page - 1) % len(embeds)
                await message.edit(embed=embeds[current_page])
                await interaction.response.defer()

            async def next_button_callback(interaction: discord.Interaction):
                nonlocal current_page
                current_page = (current_page + 1) % len(embeds)
                await message.edit(embed=embeds[current_page])
                await interaction.response.defer()

            prev_button.callback = prev_button_callback
            next_button.callback = next_button_callback

            view = View()
            view.add_item(prev_button)
            view.add_item(next_button)
            await message.edit(view=view)


async def setup(bot):
    await bot.add_cog(HelpCommand(bot))
