import discord
from discord.ext.commands import Bot
import botcoms
import os

""" from dotenv import load_dotenv
load_dotenv()"""


bot = Bot(command_prefix='$')


@bot.event
async def on_ready():
	print(f'Bot connected as {bot.user}')

#running the commands file everytime a message is sent
@bot.event
async def on_message(message):
    lowmsg = message.content.lower()
    await botcoms.command(message,lowmsg)

#starting bot up with the key
bot.run(os.getenv("DISCORD_KEY"))