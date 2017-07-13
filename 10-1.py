# -*- coding: utf-8 -*-
# PN: gasoline db, Created Feb. 2017
# Version 1.0
# KW: crawler, database create, plotting
# --------------------------------------------------- libs import
import sqlite3
conn = sqlite3.connect('gasoline.sqlite')
from bs4 import BeautifulSoup
import requests
import numpy as np
import matplotlib.pyplot as plt
# --------------------------------------------------- disp_menu()
def disp_menu():
	print("中油歷年油價查詢系統")
	print("--------------------")
	print("1. 從網站載入最新油價")
	print("2. 顯示歷年油價資訊")
	print("3. 最近10週油價資訊")
	print("4. 油價走勢圖")
	print("0. 結束")
	print("--------------------")
# --------------------------------------------------- fetch_data()
def fetch_data():
	url = 'http://new.cpc.com.tw/division/mb/oil-more4.aspx'

	html = requests.get(url).text
	sp = BeautifulSoup(html, 'lxml')
	# crawl specific data
	data = sp.find_all('span', {'id':'Showtd'})
	rows = data[0].find_all('tr')

	prices = list()
	for row in rows:
		cols = row.find_all('td')
		if len(cols[1].text) > 0:
			item = [cols[0].text, cols[1].text, cols[2].text, cols[3].text]
			prices.append(item)

	for p in prices:
		sqlstr = "select * from prices where gdate='{}'".format(p[0])
		cursor = conn.execute(sqlstr)
		if len(cursor.fetchall()) == 0:
			g92 = 0 if p[1] == '' else float(p[1])
			g95 = 0 if p[2] == '' else float(p[2])
			g98 = 0 if p[3] == '' else float(p[3])
			sqlstr = "insert into prices values('{}', {}, {}, {})".format(p[0], g92, g95, g98)
			print(sqlstr)
			conn.execute(sqlstr)
			conn.commit()
	print("Crawl finish!")
# --------------------------------------------------- disp_10data()
def disp_10data():
	cursor = conn.execute('select * from prices order by gdate desc;')    # desc => descending date
	n = 0
	for row in cursor:
		print("日期: {}，92無鉛: {}，95無鉛: {}，95無鉛: {}".format(row[0], row[1], row[2], row[3]))
		n += 1
		if n == 10:
			break
# --------------------------------------------------- chart()
def chart():
	data = []
	cursor = conn.execute("select * from prices order by gdate;")
	for row in cursor:
		data.append(list(row))
	x = np.arange(0, len(data))
	dataset = [list(), list(), list()]
	for i in range(0, len(data)):
		for j in range(0, 3):
			dataset[j].append(data[i][j+1])
	w = np.array(dataset[0]) 
	y = np.array(dataset[1])
	z = np.array(dataset[2])
	plt.ylabel("NTD$")
	plt.xlabel("Weeks ( {} --- {} )".format(data[0][0], data[len(data)-1][0]))	# len(data) - 1 -> last item
	plt.plot(x, w, color="blue", label="92")
	plt.plot(x, y, color="red", label="95")
	plt.plot(x, z, color="green", label="98")
	plt.xlim(0, len(data))
	plt.ylim(10, 40)
	plt.title("Gasoline Prices Trend (Taiwan)")
	plt.legend()
	plt.show()
# --------------------------------------------------- disp_alldata()
def disp_alldata():
	cursor = conn.execute('select * from prices order by gdate desc;')    # desc => descending date
	n = 0
	for row in cursor:
		print("日期: {}，92無鉛: {}，95無鉛: {}，95無鉛: {}".format(row[0], row[1], row[2], row[3]))
		n += 1
		if n == 20:
			x = input("請按 Enter 繼續 ...(Q: 回主選單)")
			if x == 'Q' or x == 'q':
				break
				n = 0
# --------------------------------------------------- main menu
while True:
	disp_menu()
	choice = int(input("請輸入您的選擇:"))
	if choice == 0:
		break
	elif choice == 1:
		fetch_data()
	elif choice == 2:
		disp_alldata()
	elif choice == 3:
		disp_10data()
	elif choice == 4:
		chart()
	else:
		break
	x = input("Press Enter")