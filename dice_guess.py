# dice throw

from random import randint

result = (randint(1, 6))

guess = input('Guess the number: ')
try:
	if int(guess) == result:
		print('You got it right!')
	else:
		while int(guess) != result:
			print('Wrong!\n')
			guess = input('Guess the number: ')
			if int(guess) == result:
				print('You got it right!')
				break
except:
	print('\nPlease enter a number.')