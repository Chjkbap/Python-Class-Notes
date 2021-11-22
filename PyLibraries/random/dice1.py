from random import randint  # import library

# randNumber = randint(1,6)
# print(randNumber)

dice1 = randint(1,6)
dice2 = randint(1,6)
# print(f"You threw {dice1} and {dice2} ")

die =  dice1 + dice2
if dice1 == dice2:
    print(f"You threw a double {dice1} {dice2}")
else: 
    print(f"You threw {dice1} and {dice2} ")