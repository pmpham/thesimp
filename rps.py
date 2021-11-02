import random

status = "Yes"
totalWins=0
totalLosses=0
totalTies=0
choices=["Rock","Paper","Scissors"]

while status == "Yes":
    playerChoice =""
    while choices.count(playerChoice)==0:
        playerChoice = input("Pick Rock, Paper, or Scissors and press enter")
        playerChoice = playerChoice.capitalize()

    print("successfully chosen")

    npcChoice = choices[random.randint(0,2)]
    print (f"The computer chose {npcChoice.lower()}!")

    if playerChoice == "Rock" and npcChoice == "Rock":
        print("Tie!")
        totalTies+=1
    elif playerChoice == "Rock" and npcChoice == "Paper":
        print("You Lose :(")
        totalLosses+=1
    elif playerChoice == "Rock" and npcChoice == "Scissors":
        print("You Win!")
        totalWins+=1
    elif playerChoice == "Paper" and npcChoice == "Rock":
        print ("You Win!")
        totalWins+=1
    elif playerChoice == "Paper" and npcChoice == "Paper":
        print ("Tie!")
        totalTies+=1
    elif playerChoice == "Paper" and npcChoice == "Scissors":
        print ("You Lose :(")
        totalLosses+=1
    elif playerChoice == "Scissors" and npcChoice == "Rock":
        print ("You Lose :(")
        totalLosses+=1
    elif playerChoice == "Scissors" and npcChoice == "Paper":
        print ("You Win!")
        totalWins+=1
    elif playerChoice == "Scissors" and npcChoice == "Scissors":
        print ("Tie!(")
        totalTies+=1
        

    status = (input("Type yes to continue enter to exit")).capitalize()
        
print("Game ended")
print(f"Win Loss Ratio is {totalWins}:{totalLosses}")
print(f"Total Ties: {totalTies}")