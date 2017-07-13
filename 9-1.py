# -*- coding: utf-8 -*-
# PN: SQLite practice(Students' info database), Created Feb, 2017
# Version 1.0
# KW: urlparse, netloc, path, query split
# Link: 
# --------------------------------------------------- lib import
from urllib.parse import urlparse
# --------------------------------------------------- start
url = "https://www.most.gov.tw/folksonomy/list?menu_id=ba3d22f3-96fd-4adf-a078-91a05b8f0166&filter_uid=none&listKeyword=&pageNum=2&pageSize=18&view_mode=listView&subSite=main&l=ch&tagUid="

uc = urlparse(url)
print("NetLoc:", uc.netloc) # 網域名稱
print("Path:", uc.path) # 網頁所在位置和網頁檔案名稱
# --------------------------------------------------- 網址查詢命令
q_cmds = uc.query.split('&')	# query 查詢命令
print("Query Commands:")
for cmd in q_cmds:
	print(cmd)