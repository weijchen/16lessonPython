# -*- coding: utf-8 -*-
# PN: 16 lesson python - fp open, with open as fp, readlines, Created Mar, 2017
# Version 1.0
# KW: store dictionary
# Link: 
# --------------------------------------------------- lib import
import sys
# --------------------------------------------------- start
if len(sys.argv) < 2:
	print("使用方法: python 8-4.py 成績檔案")
	exit(1)
# --------------------------------------------------- create dictionary
no = 1
scores = dict()

while True:
	score = int(input('請輸入第 {} 號的成績: (-1 結束)'.format(no)))
	if score == -1: break
	scores[no] = score
	no += 1
# --------------------------------------------------- write dictionary as txt
with open(sys.argv[1], 'w') as fp:
	fp.write(str(scores))
	
print("{} 已被儲存完畢".format(sys.argv[1]))
