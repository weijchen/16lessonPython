# -*- coding: utf-8 -*-
# PN: 16 lesson python - fp open, readlines, Created Mar, 2017
# Version 1.0
# KW: 
# Link: 
# --------------------------------------------------- lib import
import sys
# --------------------------------------------------- start
if len(sys.argv) < 2:
	print("使用方法: python 8-2.py 學生班級")
	exit(1)

std_data = dict()

with open(sys.argv[1], encoding = 'utf-8') as fp:
	alldata = fp.readlines()	#read(), readline(), readlines()

for item in alldata:
	no, name = item.rstrip('\n').split(',')	# delete \n, replaced with ,
	std_data[no] = name
print(std_data)