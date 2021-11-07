import rps
import riotcoms

async def command(message, msgstring):
    if not (message.author.bot):
        if msgstring == 'test':
            await message.channel.send('Testing 1 2 3!')
            print(f"{message.author.name}#{message.author.discriminator} said test")

        if "sex" in msgstring:
            await message.channel.send('sex is for virgins')
            print(f"{message.author.name}#{message.author.discriminator} said sex")
        if msgstring == "!about":
            await message.channel.send("This is a personal project developed by Peter to learn more about Git and Python.\nUse !dev to learn more about Peter!")
            print(f"{message.author.name}#{message.author.discriminator} used !about")

        if msgstring == "!dev":
            await message.channel.send("I am a CS student at CSULB hoping to further my knowledge and become a programmer in the future\nCheck out my Linktree! https://linktr.ee/petermpham")
            print(f"{message.author.name}#{message.author.discriminator} used !dev")

        if "!rps" in msgstring:
            await rps.rps(message,msgstring)

        if "!lol" in msgstring:
            await message.channel.send(riotcoms.player(msgstring[msgstring.index("!lol")+5:]).newleaguesearch())
        
        if "!sum" in msgstring:
            await message.channel.send(riotcoms.leaguesearch(msgstring[msgstring.index("!sum")+5:]))

        if "!tft" in msgstring:
            await message.channel.send(riotcoms.leaguesearch(msgstring[msgstring.index("!tft")+5:]))