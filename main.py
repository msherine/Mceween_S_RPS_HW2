from random import randint

# add player and computer lives

playerLives = 5
computerLives = 5

# save the player as a varible called player
# the value of the player will be one of three choices to type (input)
player = input("Choose your weapon: rock, paper or scissors: ")

print("player chose: " + player)

# an array is just a container. It holds multiple values in a 0-based index
# you can store anything in an array and retrive it later. Arrays have a square bracket notation
choices = ["rock", "paper", "scissors"]

computer = choices[randint(0,2)]

print("computer chose: " + computer)

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
