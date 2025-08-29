from random import randint
from time import sleep
from operator import itemgetter

game = {}
print(f'------Dice Rolling------')
for k in range(1, 5):
	key = f'Player {k}'
	value = randint(1, 6)
	game[key] = value
	print(f'The {key} rolled {value} on the dice')
	sleep(1)

ranking = sorted(game.items(), key=itemgetter(1), reverse=True)

print('------Ranking------')
for indx, value in enumerate(ranking):
	indx + 1
	print(f'{value[0].capitalize()}: {value[1]}')