import rps

async def command(message, msgstring):
    botids = [904955459650338857, 892480198921031700]
    if message.author.id not in botids:
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
            ids = [278364691531694082,228283737660456972]
            if message.author.id in ids:
                message.channel.send("i dont play with shitters")
            else:
                await rps.rps(message,msgstring)
    
