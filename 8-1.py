# -*- coding: utf-8 -*-
# PN: 16 lesson python - fp open, readlines, Created Mar, 2017
# Version 1.0
# KW: 
# Link: 
# --------------------------------------------------- program
fp = open("zen.txt", "r")
zops = fp.readlines()	# read as a list
fp.close()
print(zops)
i = 1
print('The Zen of Python')

for zen in zops:
	print("zen {}: {}".format(i, zen), end="")
	i += 1