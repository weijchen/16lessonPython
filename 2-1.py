# -*- coding: utf-8 -*-
# PN: 16 lesson python - input(), Created Feb, 2017
# Version 1.0
# KW: input()
# Link: 
# --------------------------------------------------- lib import
age = int(input("age = "))    # input value will be put into age

if age >= 20:
	print("今年要去投票哦")
else:
	diff = (20 - age)
	print("再過 {} 年就可以投票啦".format(diff))