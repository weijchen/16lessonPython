# -*- coding: utf-8 -*-
# PN: 16 lesson python - filter for prime, Created Mar, 2017
# Version 1.0
# KW: for, filter()
# Link: 
# --------------------------------------------------- lib import
import sympy

a, b = 500, 600
numbers = range(a, b)

prime_numbers = filter(sympy.isprime, numbers)	# use filter for numbers to check whether is prime number

print("Prime numbsers({}-{})".format(a, b))

for prime_number in prime_numbers:
	print(prime_number, end = ",")
print()