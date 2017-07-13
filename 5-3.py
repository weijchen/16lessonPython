# -*- coding: utf-8 -*-
# PN: 16 lesson python - number guess, Created Mar, 2017
# Version 1.0
# KW: random, number guess
# Link: 
# --------------------------------------------------- lib import
import random
import numpy as np
# --------------------------------------------------- initial setting
game_count = 0
all_counts = []	# calc total guessing
# --------------------------------------------------- game start
while True:
	game_count += 1
	guess_count = 0
	answer = random.randint(0, 99)
	while True:
		guess = int(input("Key in a number(0-99) = "))
		guess_count += 1
		if guess == answer:
			print("Congraduation!")
			print("您總共猜了" + str(guess_count) + "次")
			all_counts.append(guess_count)
			break;
		elif guess > answer:
			print("Too big")
		else:
			print("Too small")

	onemore = input("Play again? (Y/N)")	# create replay funciton

	if onemore != 'Y' and onemore != 'y':
		print("Your score: ")
		print(all_counts)
		print("平均猜中次數" + str(np.average(all_counts)))
		break;
