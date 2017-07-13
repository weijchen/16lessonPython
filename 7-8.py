# -*- coding: utf-8 -*-
# PN: 16 lesson python - break, Created Mar, 2017
# Version 1.0
# KW: break, while
# Link: 
# --------------------------------------------------- lib import
import random
# --------------------------------------------------- program
while True:
	x = random.randint(1, 100)
	print(x)
	if x == 6: break	# break will end up function's processing
