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
killed = 0

def monster_easy(health, food, turn, killed):
	chance = randint(0, 2)
	if chance == 2:
		m_health = 2
		print('You have been attacked!')
		print('Monster has', m_health, 'health.')
		while m_health != 0:
			health -= 1
			m_health = m_health - attack
			print("You attacked!")
			print("Monster now has", m_health, "health left, and you have", health, "left.")
			if health == 0:
				print("You were killed! Try again.")
				break
		if m_health == 0:
			print('You have defeated the monster!')
			food += 1
			turn += 1
			killed += 1
			print('You now have', food, "food, and", health, "health.")

# function templates
	# monster_easy(health, food, turn)

print("""Welcome! Try to survive as long as you can! First, you'll want to craft some weapons so that oyu can defend yourself from monsters.\n Type 'craft' to get a list of things you can make.""")

while health > 0:
	command = input('\nWhat do you want to do? ')
	if command == 'craft':
		print("""		* Wooden sword - 6 wood
		* Stone sword - 10 stone
		* Diamond sword - 4 diamonds
		* Wooden pickaxe - 4 wood
		* Stone pickaxe - 6 stone
		* Diamond pickaxe - 3 diamonds""")

if health == 0:
	print('You died! You survived', turns, 'turns, and killed', killed, "monsters.")