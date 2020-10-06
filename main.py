import discord
from discord.ext import commands

token = "NzYxMjM0NjE1MzcyNzQyNjU2.X3Xo-w.u6FCFMfiTNonMf-7yi1yQesaisk"
channel_id = 761972711551270952
prefix = "eve "

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

@client.command()
async def gay(ctx):
   await ctx.send("Fajri is gay")

@client.command()
async def check(ctx):
   embed = discord.Embed(title = "Parasite Eve", colour = discord.Colour(0x2eca6a))
   embed.add_field(name="IP", value="play.parasiteeve.xyz", inline=True)
   embed.add_field(name="Port", value="19132", inline=True)
   await ctx.send(embed=embed)

client.run(token)
