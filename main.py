from config import *
import discord
from discord.ext import commands


client = commands.Bot(prefix)

client.load_extension("cogs.commands")
client.load_extension("cogs.events")


client.run(token)
