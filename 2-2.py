# -*- coding: utf-8 -*-
# PN: 16 lesson python - datetime, Created Feb, 2017
# Version 1.0
# KW: datetime
# Link: 
# --------------------------------------------------- lib import
import datetime
# --------------------------------------------------- value input
today = datetime.date.today()
month = int(input("請問是在哪一個月份出生? "))
day = int(input("請問是在哪一天出生? "))
birthday = datetime.date(today.year, month, day)
# --------------------------------------------------- program running
if birthday < today:
	birthday = datetime.date(today.year + 1, month, day)	# 若生日已過，計算下一年

diff = birthday - today
if diff.days == 0:
	print("Yo~ Happy Birthday!!!")
else:
	print("挖! 再過" + str(diff.days) + "就是你的生日囉~")
