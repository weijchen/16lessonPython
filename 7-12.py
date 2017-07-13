# -*- coding: utf-8 -*-
# PN: 16 lesson python - try except, error test, Created Mar, 2017
# Version 1.0
# KW: try except, error test
# Link: 
# --------------------------------------------------- lib import
import os, sys
# --------------------------------------------------- program
try:
	os.remove("hello.txt")
except Exception as e:
	print(e)

	e_type, e_value, e_tb = sys.exc_info()
	print("種類: {}\n訊息: {}\n資訊: {}".format(e_type, e_value, e_tb))
