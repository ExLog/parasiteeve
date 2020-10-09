from config import *
import discord
import aiofiles
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(prefix, intents=intents)

startup_extension = ("cogs.commands",)
for ext in startup_extension:
    bot.load_extension(ext)

#bot events
@bot.event
async def on_ready():
    print("Your bot is ready.")
    bot.reaction_roles = []
    bot.welcome_channels = {} # store like {guild_id : (channel_id, message)}
    bot.goodbye_channels = {}
    
    for file in ["reaction_roles.txt", "welcome_channels.txt", "goodbye_channels.txt"]:
        async with aiofiles.open(file, mode="a") as temp:
            pass

    async with aiofiles.open("reaction_roles.txt", mode="r") as file:
        lines = await file.readlines()
        for line in lines:
            data = line.split(" ")
            bot.reaction_roles.append((int(data[0]), int(data[1]), data[2].strip("\n")))

    async with aiofiles.open("welcome_channels.txt", mode="r") as file:
        lines = await file.readlines()
        for line in lines:
            data = line.split(" ")
            bot.welcome_channels[int(data[0])] = (int(data[1]), " ".join(data[2:]).strip("\n"))

    async with aiofiles.open("goodbye_channels.txt", mode="r") as file:
        lines = await file.readlines()
        for line in lines:
            data = line.split(" ")
            bot.goodbye_channels[int(data[0])] = (int(data[1]), " ".join(data[2:]).strip("\n"))


@bot.event
async def on_member_join(member):
    for guild_id in bot.welcome_channels:
        if guild_id == member.guild.id:
            channel_id, message = bot.welcome_channels[guild_id]
            await bot.get_guild(guild_id).get_channel(channel_id).send(f"{message} {member.mention} Welcome to **{member.guild.name}**! Please read <#728879463156285471> and react to get role. ")
            return

@bot.event
async def on_member_remove(member):
    for guild_id in bot.goodbye_channels:
        if guild_id == member.guild.id:
            channel_id, message = bot.goodbye_channels[guild_id]
            await bot.get_guild(guild_id).get_channel(channel_id).send(f"{member.mention} {message}")
            return


bot.run(token)

