import discord
from config import *
from discord.ext import commands

exception = ["ExLog", "exlog", "doni", "dony"]

class Commands(commands.Cog):
   def __init__(self, client):
      self.client = client


   @commands.command()
   async def gay(self, ctx, username):
      if username in exception:
         await ctx.send("no u")
         await ctx.send(f"{ctx.message.author} is gay")
      await ctx.send(f"{username} is gay")

   @commands.command()
   async def check(self, ctx):
      embed = discord.Embed(title = "Parasite Eve", colour = discord.Colour(0x390c51))
      embed.add_field(name="IP", value="play.parasiteeve.xyz", inline=True)
      embed.add_field(name="Port", value="19132", inline=True)
      await ctx.send(embed=embed)

   @commands.command()
   @commands.has_permissions(manage_messages=True)
   async def clear(self, ctx, amount : int):
      await ctx.channel.purge(limit = amount)

   @commands.Cog.listener()
   async def on_command_error(self, ctx, error):
      if isinstance(error, commands.MissingPermissions):
         await ctx.send("You don't have permission to do the command!")

   @clear.error
   async def clear_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
         await ctx.send("Please specify an amount of messages to delete.")


def setup(client):
   client.add_cog(Commands(client))
         