from random import randint
wins = 0
loses = 0
turns = 0
draws = 0

while turns < 10:
	player = input("Rock, paper or scissors? ")
	turns += 1
	
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
		draws += 1
		
	# computer = paper
	elif computer == 'paper' and player == 'scissors':
		print("You win!")
		wins += 1
	elif computer == 'paper' and player == 'paper':
		print("You draw!")
		draws += 1
	elif computer == 'paper' and player == 'rock':
		print("You lose!")
		loses += 1
		
	# computer = scissors
	elif computer == 'scissors' and player == 'scissors':
		print("You draw!")
		draws += 1
	elif computer == 'scissors' and player == 'paper':
		print("You win!")
		wins += 1
	elif computer == 'scissors' and player == 'rock':
		print("You lose!")
		loses += 1
		
print('You won', wins, "times, and lost", loses, "times. You drew", draws, "times.")