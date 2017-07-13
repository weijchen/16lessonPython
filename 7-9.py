# -*- coding: utf-8 -*-
# PN: 16 lesson python - map(), Created Mar, 2017
# Version 1.0
# KW: for, map()
# Link: 
# --------------------------------------------------- lib import


def pick(x):
	fruits = ['Apple', 'Banana', 'Orange', 'Tomato', 'Pine Apple', 'Berry']
	return fruits[x]

alist = [1, 4, 2, 5, 0, 3, 4, 4, 2]
# map("執行用函數","容器變數")
choices = map(pick, alist)	# use alist as the index to choose from fruits, throw alist into pick function

for choice in choices:
	print(choice)