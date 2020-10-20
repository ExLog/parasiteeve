from config import *
import os
import sys

import aiofiles
from discord.ext import commands

sys.path.append(os.path.abspath(os.path.join('/')))


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.bot.user} has logged in.")
        self.bot.welcome_channels = {}
        self.bot.goodbye_channels = {}

        for file in ["welcome.txt", "goodbye.txt"]:
            async with aiofiles.open(file, mode="a") as temp:
                pass

        async with aiofiles.open("./welcome.txt", mode="r") as file:
            lines = await file.readlines()
            for line in lines:
                data = line.split(" ")
                self.bot.welcome_channels[int(data[0])] = (
                    int(data[1]), " ".join(data[2:]).strip("\n"))

        async with aiofiles.open("./goodbye.txt", mode="r") as file:
            lines = await file.readlines()
            for line in lines:
                data = line.split(" ")
                self.bot.goodbye_channels[int(data[0])] = (
                    int(data[1]), " ".join(data[2:]).strip("\n"))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        for guild_id in self.bot.welcome_channels:
            if guild_id == member.guild.id:
                channel_id, message = self.bot.welcome_channels[guild_id]
                await self.bot.get_guild(guild_id).get_channel(channel_id).send(f"Hey {member.mention} Welcome to **{member.guild.name}**! Please read <#728879463156285471> and react to get role.")
                return

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        for guild_id in self.bot.goodbye_channels:
            if guild_id == member.guild.id:
                channel_id, message = self.bot.goodbye_channels[guild_id]
                await self.bot.get_guild(guild_id).get_channel(channel_id).send(f"{member.mention} just left the server.")
                return


def setup(bot):
    bot.add_cog(Events(bot))
