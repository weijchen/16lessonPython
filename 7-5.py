# -*- coding: utf-8 -*-
# PN: 16 lesson python - 9*9 chart, Created Mar, 2017
# Version 1.0
# KW: for, 9*9
# Link: 
# --------------------------------------------------- python 2
for i in range(1,10,3):
	for j in range(1,10):
		print('%d * %d = %d    ' %(i, j, i*j), end="")
		print('%d * %d = %d    ' %(i+1, j, (i+1)*j), end="")
		print('%d * %d = %d    ' %(i+2, j, (i+2)*j))
	print()
# ------------------------------------------------- python 3
for i in range(1,10,3):
	for j in range(1,10):
		print('{}*{} = {:>2}    ' .format(i, j, i*j), end="")
		print('{}*{} = {:>2}    ' .format(i+1, j, (i+1)*j), end="")
		print('{}*{} = {:>2}    ' .format(i+2, j, (i+2)*j))
	print()