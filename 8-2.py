# -*- coding: utf-8 -*-
# PN: 16 lesson python - fp open, readlines, Created Mar, 2017
# Version 1.0
# KW: 
# Link: 
# --------------------------------------------------- lib import
import sys
# --------------------------------------------------- start
print("參數長度 = {}".format(len(sys.argv)))
i = 0

for arg in sys.argv:
	print("第 {} 個參數為: {}".format(i, arg))
	i += 1

