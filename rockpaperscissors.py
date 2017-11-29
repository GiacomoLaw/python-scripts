from random import randint

player = input("Rock, paper or scissors? ")
wins = 0
loses = 0

computer = randint(1, 3)
if computer == 1:
	computer = 'rock'
elif computer == 2:
	computer = 'paper'
else:
	computer = 'scissors'
	
print("You chose", player, "and the computer chose", computer)


# computer = rock
if computer == 'rock' and player == 'scissors':
	print("You lose!")
	loses += 1
elif computer == 'rock' and player == 'paper':
	print("You win!")
	wins += 1
elif computer == 'rock' and player == 'rock':
	print("You draw!")
	
# computer = paper
elif computer == 'paper' and player == 'scissors':
	print("You win!")
	wins += 1
elif computer == 'paper' and player == 'paper':
	print("You draw!")
elif computer == 'paper' and player == 'rock':
	print("You lose!")
	loses += 1
	
# computer = scissors
elif computer == 'scissors' and player == 'scissors':
	print("You draw!")
elif computer == 'scissors' and player == 'paper':
	print("You win!")
	wins += 1
elif computer == 'scissors' and player == 'rock':
	print("You lose!")
	loses += 1