# -*- coding: utf-8 -*-
# PN: 
# Version 1.0
# KW: 
# --------------------------------------------------- libs import
from bs4 import BeautifulSoup as bs
import requests, sys
# --------------------------------------------------- 
url = 'http://new.cpc.com.tw/division/mb/oil-more4.aspx'
# --------------------------------------------------- find span with id Showtd and the content
html = requests.get(url).text
sp = bs(html, 'html.parser')
data = sp.find_all('span', {'id':'Showtd'})
rows = data[0].find_all('tr')
# --------------------------------------------------- put content into list(prices)
prices = list()
for row in rows:
	cols = row.find_all('td')
	if len(cols[1].text) > 0:
		item = [cols[0].text, cols[1].text, cols[2].text, cols[3].text]
		prices.append(item)
# --------------------------------------------------- print result
print(['調價日期','無鉛汽油 92','無鉛汽油 95','無鉛汽油 98'])
for p in prices:
	print(p)