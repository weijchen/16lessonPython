# -*- coding: utf-8 -*-
# PN: 16 lesson python - module create, Created Mar, 2017
# Version 1.0
# KW: function, import
# Link: 
# --------------------------------------------------- lib import
def draw(n, symbol = '*'):
	for i in range(1, n + 1):
		print(symbol, end = '')
	print()