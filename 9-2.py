# -*- coding: utf-8 -*-
# PN: SQLite practice(Students' info database), Created Feb, 2017
# Version 1.0
# KW: requests.get(), encoding problems
# Link: 
# --------------------------------------------------- lib import
import requests
url = 'https://udn.com/news/story/10858/2315252'
html = requests.get(url).text.splitlines()

for i in range(0, 15):
	print(html[i])