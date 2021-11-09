from random import randint

choices = ["rock", "paper", "scissors"]

# player will be the weapon and the player will choose via input
player = False

# these lives need to decrement when a player chooses via input 
playerLives = 5
computerLives = 5


def winorlose(status):
	print("You " + status + "! Would you like to play again?")
	choice = input(" Y / N? ")

	global playerLives
	global computerLives
	global player

	if choice == "n":
		print(" Better luck next time!")
		exit()
	# reset and restart
	else:
		playerLives = 5
		computerLives = 5
		player = False

# create an infinite loop 
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

	print("player life count: " + str(playerLives))
	print("computer life count: " + str(computerLives))

	if playerLives == 0:
		winorlose("lost")

	elif computerLives == 0:
		winorlose("won")

	player = False
