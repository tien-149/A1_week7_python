from random import randint

player_lives = 5
computer_lives = 5

#avaikable weapons => Store this is an array
choices = ["Rock","Paper","Scissors"]
player = False

# Make the computer pick one item at random
computer = choices[randint(0, 2)]

#Show the computer's choice in the terminal window
print("Computer chooses: ",computer)

while player is False:
	print("====================================")
	print("====================================")
	player = input("Rock,Paper or Scissors? \n")
	print("Player chooses:", player)

if(player== computer):
	print("Tie!Live to shoot another day")

elif player == "Rock":
		if computer == "Paper":
			# computer won
			player_lives -= 1
			print("You lose", computer,"covers", player)
		else:
			print("You win",player,"smashes",computer)
			computer_lives -= 1

elif player=="Paper":
		if computer == "Scissor":
			player_lives -= 1
			print("You lose", computer,"cuts", player)
		else:
			print("You win",player,"covers",computer)
			computer_lives -= 1

elif player=="Scissor":
		if computer == "Rock":
			player_lives -= 1
			print("You lose", computer,"smashes", player)
		else:
			print("You win",player,"cuts",computer)
			computer_lives -= 1

elif player == "Quit":
	exit()

else:
	print("Not a valid option. Check again and check your spelling!\n")

	player == False
	computer = choices[randint(0, 2)]











