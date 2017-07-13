# -*- coding: utf-8 -*-
# PN: 16 lesson python - for if, Created Mar, 2017
# Version 1.0
# KW: for, if
# Link: 
# --------------------------------------------------- lib import
# dictionary: {key: value}
stock = {'book': 10, 'pen': 3, 'earser': 6, 'ruler': 2}

for key, value in stock.items():
	if value > 5:
		print("({}, {})".format(key, value))
