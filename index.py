import discord
from discord.ext.commands import Bot
import botcoms

""" from dotenv import load_dotenv
load_dotenv()"""
import os

bot = Bot(command_prefix='$')
TOKEN = '<INSERT TOKEN HERE>'

@bot.event
async def on_ready():
	print(f'Bot connected as {bot.user}')
	
@bot.event
async def on_message(message):
    lowmsg = message.content.lower()
    await botcoms.command(message,lowmsg)


		
bot.run(os.getenv("DISCORD_KEY"))