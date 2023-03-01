from discord.ext import commands
from discord import Intents


# How the bot will be called:
# E.g. = >hello
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
    
    if "bot revolution" in message.content: # message.author.name
        await message.channel.send(
            f"Excuse me, what did u just say, mister {message.author.name}?"
        )

        await message.delete()
    
    await bot.process_commands(message)

# Bot Commands:
@bot.command(name="hello")
async def say_hello(ctx):
    name: None = ctx.author.name

    response: str = f"Hello {name}, how u doing?"

    await ctx.send(response)


@bot.command(name="bye")
async def say_bye(ctx):
    name: None = ctx.author.name

    response: str = f"Bye bye {name}!"

    await ctx.send(response)


bot.run("OTM0MjE0NTE2MjM1OTg5MDk1.GEWpib.sq2fM3qweejM1dNMeu_KI4mIEjL7xoBhr1G9sY")
