import rps
import riotcoms


async def command(message, msgstring):

    #checking if message contains command and runs it
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
            await message.channel.send(riotcoms.player(msgstring[msgstring.index("!tft")+5:]).tftsearch())

        if msgstring == "!leyna":
            await message.channel.send("https://cdn.discordapp.com/attachments/814348422017712200/907523104434192384/unknown.png")
            await message.channel.send("<@556719374359068675>")

        if msgstring == "!source":
            await message.channel.send("https://github.com/pmpham/thesimp")
