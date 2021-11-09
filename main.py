from random import randint

choices = ["rock", "paper", "scissors"]

# player will be the weapon and the player will choose via input
player = False

# these lives need to decrement when a player chooses via input 
playerLives = 5
computerLives = 5

while player is False:

	player = input("Choose your weapon: rock, paper or scissors: ")
	computer = choices[randint(0, 2)]

	print("player choose: " + player)
	print("computer choose: " + computer)

	if (computer == player):
		print("Tie! Try again.")

	elif (player == "rock"):
		if (computer == "paper"):
			print("You lose!")
			playerLives = playerLives - 1
		else:
			print("You win!")
			computerLives = computerLives - 1

	elif (player == "paper"):
		if (computer == "scissors"):
			print("You lose!")
			playerLives = playerLives - 1
		else:
			print("You win!")
			computerLives = computerLives - 1

	elif (player == "scissors"):
		if (computer == "rock"):
			print("You lose!")
			playerLives = playerLives - 1
		else:
			print("You win!")
			computerLives = computerLives - 1

	print("computer lives: " + str(computerLives))
	print("player lives: " + str(playerLives))

	if playerLives == 0:
		print("You lost! Would you like to play again?")
		choice = input(" Y / N? ")

		if choice == "n":
			print(" Better luck next time!")
			exit()
			
	elif computerLives == 0:
		print(" You win!!")

	player = False
