# -*- coding: utf-8 -*-
# PN: 16 lesson python - store dictionary, Created Mar, 2017
# Version 1.0
# KW: sys, ast, with open as fp
# Link: 
# --------------------------------------------------- lib import
import sys
import ast
# --------------------------------------------------- start
if len(sys.argv) < 2:
	print("使用方式: python 8-5.py 成績檔案")
	exit(1)

scores = dict()
# --------------------------------------------------- read file's dict element

with open(sys.argv[1], 'r') as fp:
	filedata = fp.read()
	scores = ast.literal_eval(filedata)
print("以下是 {} 成績檔的字典型態資料: ".format(sys.argv[1]))
print(scores)
