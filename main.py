# main.py
import discord
from discord.ext import commands
import os
import json
import asyncio

from utils.io_utils import load

# Charger les infos
infos = load("config.json")
prefix = infos.get("prefix", "!")
token = infos.get("token")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}.")
    await bot.tree.sync()
    print("✅ Commandes slash synchronisées.")

async def load_cogs():
    for folder in ["cogs"]:
        for filename in os.listdir(folder):
            if filename.endswith(".py"):
                await bot.load_extension(f"{folder}.{filename[:-3]}")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())