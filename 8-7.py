# -*- coding: utf-8 -*-
# PN: 16 lesson python - earthquake, Created Mar, 2017
# Version 1.0
# KW: json, datetime
# Link: 
# --------------------------------------------------- lib import
import json, datetime
# --------------------------------------------------- start
fp = open('earthquake.json', 'r')
eqs = json.load(fp)

print("過去7天全球發生重大的地震資訊: ")
print()
for eq in eqs['features']:
	print("地點:{}".format(eq['properties']['place']))
	print("震度:{}".format(eq['properties']['mag']))
	et = float(eq['properties']['time']) / 1000.0
	d = datetime.datetime.fromtimestamp(et).strftime('%Y-%m-%d %H:%M:%S')
	print("時間:{}".format(d))
	print()