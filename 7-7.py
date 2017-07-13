# -*- coding: utf-8 -*-
# PN: 16 lesson python - 7-6 deform, Created Mar, 2017
# Version 1.0
# KW: 
# Link: 
# --------------------------------------------------- lib import

for i in range(2, 9):
	if i != 2 and i != 6: continue
	for j in range(1, 10):
		for k in range(i, i + 5):
			print("{} * {} = {:>2}    ".format(k, j, k * j), end = "")
		print()
	print()