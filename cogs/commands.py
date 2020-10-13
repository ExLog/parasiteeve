from config import *

import discord
from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def check(self, ctx):
        try:
            website_status = True
            # Change your SERVER_API_KEY to your own Server Key.
            api_request = requests.get(
                f"https://minecraftpocket-servers.com/api/?object=servers&element=detail&key={Server_Key_API}")
            api = json.loads(api_request.content)
            server_name = api["name"]
            ip = api["address"]
            port = api["port"]
            rank = api["rank"]
            online_now = api["is_online"]
            last_check = api["last_check"]
        except Exception:
            website_status = False

        if website_status == True:
            embed = discord.Embed(
                title=server_name, colour=discord.Colour(0x390c51))
            embed.add_field(name="IP", value=ip, inline=True)
            embed.add_field(name="Port", value=port, inline=True)
            embed.add_field(name="Players Online",
                            value=online_now, inline=False)
            embed.set_footer(text=last_check)
            await ctx.send(embed=embed)
        else:
            await ctx.send("The API is not Available")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to do the command!")

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify an amount of messages to delete.")


def setup(bot):
    bot.add_cog(Commands(bot))
