# -*- coding: utf-8 -*-

from discord.ext import commands
import discord

class Welcome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = self.bot.get_channel(941682534843023370)

        if not channel:
            return

        await channel.send(f"Welcome, !")

def setup(bot):
    bot.add_cog(Welcome(bot))
