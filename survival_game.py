# Survival game
# INCOMPLETE

from random import randint

food = 0
water = 0
wood = 0
stone = 0
diamond = 0

attack = 0
defense = 1
health = 10

turn = 0

def monster_easy(food, turn):
    chance = randint(0, 2)
    if chance == 2:
        m_health = 2
        while m_health != 0:
            print('You have been attacked!')
            print('Monster has', m_health, 'health left.')
            health = 9
            m_health = m_health - attack
            print("Monster now has", m_health, "health")
            if health == 0:
                print("You were killed! Try again.")
                break
        else m_health == 0:
            print('You have defeated the monster!')
            food += 1
            turn += 1
            print('You now have', food, "food, and", health, "health.")
    return food

monster_easy(food, turn)
