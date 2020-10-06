import discord
from discord.ext import commands
from os import getenv

token = getenv('TOKEN')
channel_id = int(getenv('CHANNEL'))
prefix = getenv('PREFIX')

client = commands.Bot(prefix)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("Minecraft"))
    print("{} has logged in.".format(client.user))


@client.event
async def on_member_join(member):
   await client.get_channel(channel_id).send(f"Hey {member.mention} Welcome to **{member.guild.name}**! Please read <#728879463156285471> and react to get role.")


@client.event
async def on_member_remove(member):
   await client.get_channel(channel_id).send(f"{member.name}#{member.discriminator} just left the server.")

client.run(token)
