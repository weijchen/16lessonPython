# -*- coding: utf-8 -*-
# PN: 16 lesson python - while loop, Created Mar, 2017
# Version 1.0
# KW: while
# Link: 
# --------------------------------------------------- lib import
import random
# --------------------------------------------------- program
x = random.randint(1, 6)
print(x)

# break if x == 6
while x != 6:
	x = random.randint(1, 6)
	print(x)