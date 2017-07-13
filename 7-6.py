# -*- coding: utf-8 -*-
# PN: 16 lesson python - loop three layers, Created Mar, 2017
# Version 1.0
# KW: for
# Link: 
# --------------------------------------------------- lib import

for i in range(2, 7, 4):
	for j in range(1, 10):
		for k in range(i, i + 5):
			print("{} * {} = {:>2}    ".format(k, j, k * j), end = "")
		print()
	print()