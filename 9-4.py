# -*- coding: utf-8 -*-
# PN: Email regex prac, Created Feb, 2017
# Version 1.0
# KW: email, find, regex, findall
# Link:
# --------------------------------------------------- lib import
import requests, re
# --------------------------------------------------- start

url = 'http://www.taifex.com.tw/chinese/2/TFO.asp'
html = requests.get(url).text

regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+)"	# regex for email
emails = re.findall(regex, html)

for email in emails:
	print(email)