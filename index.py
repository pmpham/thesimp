import discord
from discord.ext.commands import Bot
import botcoms

bot = Bot(command_prefix='$')
TOKEN = '<INSERT TOKEN HERE>'

@bot.event
async def on_ready():
	print(f'Bot connected as {bot.user}')
	
@bot.event
async def on_message(message):
    lowmsg = message.content.lower()
    await botcoms.command(message,lowmsg)


		
bot.run('OTA0OTU1NDU5NjUwMzM4ODU3.YYDDcg.zlTQVambY7XKOhKxxIavVVRIRV0')