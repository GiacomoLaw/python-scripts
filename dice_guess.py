# dice throw

from random import randint
result = (randint(1, 6))

guess = input('Guess the number: ')
if int(guess) == result:
	print('You got it right!')
else:
	while int(guess) != result:
		print('Wrong!\n')
		tryagain = input('Guess the number: ')
		if int(tryagain) == result:
			print('You got it right!')
			break