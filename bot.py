import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!")

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        """Get the bot's current websocket latency."""
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.command(name="setstatus")
    async def setstatus(self, ctx: commands.Context, *, text: str):
        """Set the bot's status."""
        await ctx.bot.change_presence(activity=discord.Game(name=text))

    @commands.command()
    async def test(ctx):
        p = {ctx.author.mention}
        await ctx.send("Pong! {p} ms")

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
       channel = self.bot.get_channel(941682534843023370)
        if not channel:
            return
        await channel.send('{member.name}, ку')

bot.run("")