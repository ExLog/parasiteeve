import os

import discord
from discord.ext import commands
from config import *

intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(prefix, intents=intents)


startup_extension = ("cogs.commands", "cogs.events")
for ext in startup_extension:
    bot.load_extension(ext)


bot.run(token)
