import random
import discord

choices=["Rock","Paper","Scissors"]


async def rps(message,msgstr):
        rpsidx = (msgstr.index("!rps"))
        playerChoice = msgstr[rpsidx+5::]
        playerChoice = playerChoice.capitalize()
        userid = message.author.id

        print(playerChoice)
        if playerChoice in choices:

            print("successfully chosen")

            npcChoice = choices[random.randint(0,2)]
            await message.channel.send(f"The computer chose {npcChoice.lower()}!")

            if playerChoice == "Rock" and npcChoice == "Rock":
                await message.channel.send("Tie!")
            elif playerChoice == "Rock" and npcChoice == "Paper":
                await message.channel.send("You Lose :(")
            elif playerChoice == "Rock" and npcChoice == "Scissors":
                await message.channel.send("You Win!")
            elif playerChoice == "Paper" and npcChoice == "Rock":
                await message.channel.send("You Win!")
            elif playerChoice == "Paper" and npcChoice == "Paper":
                await message.channel.send("Tie!")
            elif playerChoice == "Paper" and npcChoice == "Scissors":
                await message.channel.send("You Lose :(")
            elif playerChoice == "Scissors" and npcChoice == "Rock":
                await message.channel.send("You Lose :(")
            elif playerChoice == "Scissors" and npcChoice == "Paper":
                await message.channel.send("You Win!")
            elif playerChoice == "Scissors" and npcChoice == "Scissors":
                await message.channel.send("Tie!(")
        
        else:
            await message.channel.send("Choose a correct item!")