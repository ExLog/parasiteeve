from config import *
import os
import sys

import discord
from discord.ext import commands

sys.path.append(os.path.abspath(os.path.join('/')))


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("{} has logged in.".format(self.bot.user))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.bot.get_guild(server).get_channel(channel_id).send(f"Hey {member.mention} Welcome to **{member.guild.name}**! Please read <#728879463156285471> and react to get role.")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await self.bot.get_guild(server).get_channel(channel_id).send(f"{member.mention} just left the server.")


def setup(bot):
    bot.add_cog(Events(bot))
