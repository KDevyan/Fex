import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print('ready for sex')


@bot.command(name="ping")
async def ping(self, ctx: commands.Context):
    """Get the bot's current websocket latency."""
    await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")


@bot.command(name="setstatus")
async def setstatus(ctx: commands.Context, *, text: str):
    """Set the bot's status."""
    await ctx.bot.change_presence(activity=discord.Game(name=text))


@bot.command()
async def test(ctx):
    p = {ctx.author.mention}
    await ctx.send(f'Pong! {p} ms')


@bot.event
async def on_member_join(self, member: discord.Member):
    channel = self.bot.get_channel(962060712040071221)
    if not channel:
        return
    await channel.send(f'{member.name}, ку')


bot.run("OTYyMDIxNjU2OTcxMzQxODQ0.YlBefA.DSU2H2NCYx9htxqmYi3pTFj-d88")
