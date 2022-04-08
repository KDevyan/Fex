# -*- coding: utf-8 -*-

from discord.ext import commands
import discord

class Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        """Get the bot's current websocket latency."""
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.command(name="setstatus")
    async def setstatus(self, ctx: commands.Context, *, text: str):
        """Set the bot's status."""
        await ctx.bot.change_presence(activity=discord.Game(name=text))

    @commands.test("test")
    async def test(ctx):
        p = {ctx.author.mention}
        await ctx.send("Pong! {p} ms")

def setup(bot):
    bot.add_cog(Commands(bot))
