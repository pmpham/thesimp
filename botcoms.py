async def command(message, msgstring):
    botids = [904955459650338857, 892480198921031700]
    if message.author.id not in botids:
        if msgstring == 'test':
            await message.channel.send('Testing 1 2 3!')
            print(f"{message.author.name}#{message.author.discriminator} said test")

        if "sex" in msgstring:
            await message.channel.send('sex is for virgins')
            print(f"{message.author.name}#{message.author.discriminator} said sex")