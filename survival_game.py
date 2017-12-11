# Survival game
# INCOMPLETE

from random import randint

food = 0
water = 0
wood = 0
stone = 0
diamond = 0

attack = 1
defense = 1
health = 10

turn = 0

def monster_easy(health, food, turn):
	chance = randint(0, 2)
	if chance == 2:
		m_health = 2
		while m_health != 0:
			print('You have been attacked!')
			print('Monster has', m_health, 'health.')
			health -= 1
			m_health = m_health - attack
			print("Monster now has", m_health, "health left, and you have", health, "left.")
			if health == 0:
				print("You were killed! Try again.")
				break
		if m_health == 0:
			print('You have defeated the monster!')
			food += 1
			turn += 1
			print('You now have', food, "food, and", health, "health.")
	return food
	
monster_easy(health, food, turn)