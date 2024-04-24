import discord
import sys
import ezcord

try:
    bot = ezcord.Bot(intents=discord.Intents.all())
except RuntimeError as e:
    print("[[bold yellow]![/bold yellow]] > Closing session")
    sys.exit(0)

bot.load_cogs("cogs")

bot.run("Token here")
