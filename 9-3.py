# -*- coding: utf-8 -*-
# PN: SQLite practice(Students' info database), Created Feb, 2017
# Version 1.0
# KW: requests.get(), find name
# Link: 
# --------------------------------------------------- lib import
import requests
# --------------------------------------------------- start
url = 'http://www.com.tw/exam/check_0001_NO_0_101_0_3.html'
name = input("請輸入要查詢的名字 ")
html = requests.get(url).text
if name in html:
	print("yes")
else:
	print("no")