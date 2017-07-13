# -*- coding: utf-8 -*-
# PN: 16 lesson python - two laters of if/elif/else, Created Mar, 2017
# Version 1.0
# KW: if/elif/else, two layers
# Link: 
# --------------------------------------------------- lib import
score = int(input("Please input your score: "))

if score >= 60:
	print("You pass the exam with ", end = "")
	if score >= 90:
		print("Grade A")
	elif score >= 80:
		print("Grade B")
	elif score >= 70:
		print("Grade C")
	elif score >= 60:
		print("Grade D")
else:
	print("Failed")