import discord
import datetime
from discord.ext import commands
from mcstatus import MinecraftServer
# K.Devyan#0777


bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())  # интенты


@bot.command()  # онлайн
async def online(ctx):
    server = MinecraftServer.lookup("query ip")
    query = server.query()
    status = server.status()
    a = ", ".join(query.players.names)
    if not a:
        a = "Сервер пуст!"
    else:
        a = ", ".join(query.players.names)
    embedonline = discord.Embed(title="Онлайн на сервере", description=f"`{status.players.online}/{status.players.max}`"
                                , color=0x3eebbe)
    embedonline.add_field(name="Игроки в сети:", value=f"`{a}`", inline=False)
    embedonline.timestamp = datetime.datetime.utcnow()
    embedonline.set_footer(text='Furex SMP\u200b')
    await ctx.reply(embed=embedonline)


@bot.event  # старт бота
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="на игроков FurexSMP"))
    # set status
    print('\n> Vanilla ● SMP\n> Furex SMP запущен\n')


@bot.command()  # пинг бота
async def ping(self, ctx: commands.Context):
    await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")


@bot.command(name="setstatus")  # смена статуса бота
@commands.has_permissions(administrator=True)  # требования для использование команды
async def setstatus(ctx: commands.Context, *, text: str):
    await ctx.bot.change_presence(activity=discord.Game(name=text))  # for fun, not use or remove this :D


@bot.command()
async def test(ctx, member: discord.Member):
    await ctx.send(f'helluw, {member.mention}!')  # a test command
    await ctx.message.delete()  # delete trigger


@bot.command()
async def de(ctx):
    embed = discord.Embed(title="FurexSMP", description="Теплые вечера у тлеющего костра, воплощение в игре больших"
                                                        "и не очень совместных проектов, постоянное взаимодействие"
                                                        "игроков, плавное, неспешное развитие, постройка городов,"
                                                        "поселений и, конечно, уютная, душевная"
                                                        "атмосфера в компании, всё это мы развиваем"
                                                        "в нашем небольшом круге друзей."
                                                        "Играй с нами!", colour=0x9b59b6)
    # colour - https://discordpy.readthedocs.io/en/latest/api.html#discord.Colour (and very bed code :D)
    embed.add_field(name="Social", value="[Вконтакте](https://vk.com/furexmc/)\n[Telegram](https://t.me/furexmc)")
    embed.add_field(name="Info", value="Правила <#941646232923811850>\nНовости <#941684622922764329>")
    embed.set_footer(text="Мы вас всех любим!", icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
    await ctx.send(embed=embed)
    await ctx.message.delete()  # delete trigger


@bot.event
async def on_member_join(self, member: discord.Member):
    channel = self.bot.get_channel(962060712040071221)
    if not channel:
        return
    await channel.send(f'{member.name}, привет! Пожалуйста, заполни заявку')  # приветствие


bot.run("your toked")
