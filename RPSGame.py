from random import randint

#available weapons => Store this is an array
choices = ["Rock","Paper","Scissors"]
continute = ["Q"]
player = False
playerLives = 1
computerLives = 1

# Make the computer pick one item at random
computer = choices[randint(0, 2)]
#Show the computer's choice in the terminal window
print("Computer chooses: ",computer)

while player == False:
	#Set player to True
	print("Choose your weapon! You only have 1 life!")
	player = input("Rock, Paper or Scissors?\n")
	print("Player chooses:",player)
	
	if (player== computer):
		print("Tie!")
		print("Play again!\n")
		player = False
		computer = choices[randint(0, 2)]

	elif player == "Rock":
		if computer == "Paper":
			# computer won
			print("You lose", computer,"covers", player, )
			playerLives -=1
			print("Player life =" , playerLives,"and", "Computer Lives =" , computerLives,)
			if playerLives == 0:
				print("Q if you want to QUIT. Or just keep playing again!\n")
				playerLives +=1
				player = False
				computer = choices[randint(0, 2)]
			# computer lose
			else:
				player = False
				computer = choices[randint(0, 2)]

		else:
			print("Player win! ",player,"smashes",computer)
			computerLives -=1
			print("Player Life = ", playerLives,"and", "Computer Lives =" , computerLives,)
			if computerLives == 0:
				print("Q if you want to QUIT. Or just keep playing again!\n")
				computerLives +=1
				player = False
				computer = choices[randint(0, 2)]
			else:
				player = False
				computer = choices[randint(0, 2)]
	elif player == "Paper":
		if computer == "Scissors":
			# computer won
			print("You lose", computer,"cuts", player, )
			playerLives -=1
			print("Player life =" , playerLives,"and", "Computer Lives =" , computerLives,)
			if playerLives == 0:
				print("Q if you want to QUIT. Or just keep playing again!\n")
				playerLives +=1
				player = False
				computer = choices[randint(0, 2)]
			else:
				player = False
				computer = choices[randint(0, 2)]

		else:
			print("Player win! ",player,"covers",computer)
			computerLives -=1
			print("Player Life = ", playerLives,"and", "Computer Lives =" , computerLives,)
			if computerLives == 0:
				print("Q if you want to QUIT. Or just keep playing again!\n")
				computerLives +=1
				player = False
				computer = choices[randint(0, 2)]
			else:
				player = False
				computer = choices[randint(0, 2)]
	elif player == "Scissors":
		if computer == "Rock":
			# computer won
			print("You lose", computer,"smashes", player, )
			playerLives -=1
			print("Player life =" , playerLives,"and", "Computer Lives =" , computerLives,)
			if playerLives == 0:
				print("Q if you want to QUIT. Or just keep playing again!\n")
				playerLives +=1
				player = False
				computer = choices[randint(0, 2)]
			else:
				player = False
				computer = choices[randint(0, 2)]

		else:
			print("Player win! ",player,"cuts",computer)
			computerLives -=1
			print("Player Life = ", playerLives,"and", "Computer Lives =" , computerLives,)
			if computerLives == 0:
				print("Q if you want to QUIT. Or just keep playing again!\n")
				computerLives +=1
				player = False
				computer = choices[randint(0, 2)]
			else:
				player = False
				computer = choices[randint(0, 2)]

	elif player == "Q":
		exit()

	else:
		print("Not a valid option. Check again and check your spelling!\n")
		player = False
		computer = choices[randint(0, 2)]








