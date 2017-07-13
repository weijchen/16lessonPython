# -*- coding: utf-8 -*-
# PN: 16 lesson python - try except, Created Mar, 2017
# Version 1.0
# KW: try except
# Link: 
# --------------------------------------------------- lib import
while True:
	# program must pass try loop to enter if loop, prevent function
	try:
		age = int(input("What is your age?"))
		break
	except:
		print("Please enter a number")

if age < 15:
	print("You are too young!")
else:
	print("Good!")