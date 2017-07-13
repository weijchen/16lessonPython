# -*- coding: utf-8 -*-
# PN: 16 lesson python - function vars, Created Mar, 2017
# Version 1.0
# KW: function
# Link: 
# --------------------------------------------------- lib import
def add2number(a, b):
	global d
	c = a + b
	d = a + b
	print("在函數中，(c = {}, d = {})".format(c, d))
	return c

c = 10
d = 99
print("呼叫函數前，(c = {}, d = {})".format(c, d))
print("{} + {} = {}".format(2, 2, add2number(2, 2)))
print("呼叫函數後，(c = {}, d = {})".format(c, d))
# c is local var, unchanged after function run
# d is global var, changed after function run
