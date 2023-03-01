from decouple import config
from discord.ext import commands
from discord import Intents

# Environment Variables (import the .env file)
TOKEN = config("TOKEN", default="###", cast=str)
ONEDRIVE_FILES = config("ONEDRIVE", default="Importe o arquivo .env", cast=str)

intents = Intents().all()
intents.members = True
bot: object = commands.Bot(command_prefix=">", intents=intents)


# Bot init (Terminal)
@bot.event
async def on_ready():
    print(f"{bot.user} on duty!")


# Bot Events:
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "bot revolution" in message.content:  # message.author.name
        await message.channel.send(
            f"Excuse me, what did u just say, mister {message.author.name}?"
        )

        await message.delete()

    await bot.process_commands(message)


# Bot Commands:
@bot.command(name=">olá")
async def say_hi(ctx):
    name: str = ctx.author.name

    response: str = f"Olá {name}, como está você?"

    await ctx.send(response)


@bot.command(name="arquivos")
async def onedrive_files(ctx: str) -> str:
    name: str = ctx.author.name

    response: str = f"Aqui estão os arquivos de aulas, {name}.\n\n{ONEDRIVE_FILES}"

    await ctx.send(response)


bot.run(TOKEN)
