import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="~", intents=discord.Intents.all())


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("test"))
    print('ready for sex')


@bot.command(name="ping")
async def ping(self, ctx: commands.Context):
    await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")


@bot.command(name="setstatus")
async def setstatus(ctx: commands.Context, *, text: str):
    await ctx.bot.change_presence(activity=discord.Game(name=text))


@bot.command()
async def test(ctx, member: discord.Member):
    await ctx.send(f'helluw, {member.mention}!')


@bot.event
async def on_member_join(self, member: discord.Member):
    channel = self.bot.get_channel(962060712040071221)
    if not channel:
        return
    await channel.send(f'{member.name}, ку')


bot.run("")
