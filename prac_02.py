# -*- coding: UTF-8 -*-

import string
import keyword
import sys
import requests
import math
from bs4 import BeautifulSoup
#import easygui

#easygui.msgbox("Welcome to Gossiping Parser")

def isNum(value):
    try:
        value + 1
    except TypeError:
        return False
    else:
        return True

def isNum2(value):
    try:
        x = int(value)
    except TypeError:
        return False
    except ValueError:
        return False
    except Exception:
        return False
    else:
        return True

n = 999
def inputWhich():
	x = input(">>> Which one do you want to see? (1~{}) or show post list (list), to exit (exit), to re-load list (refresh) : ".format(n))
	return x

ptt_domain = "https://www.ptt.cc"
payload = {
'from':'/bbs/Gossiping/index.html',
'yes':'yes'
}

rs = requests.session()
res = rs.post(ptt_domain + '/ask/over18', verify=False, data=payload)

post_list = []
連結列表 = []
清單列表 = []

def freshList():
	res = rs.get(ptt_domain + '/bbs/Gossiping/index.html', verify=False)
	print("網頁編碼 : ", res.encoding)

	# Use BeautifulSoup
	soup = BeautifulSoup(res.text)

	for entry in soup.select('.r-ent'):
		href = ""
		for a in entry.find_all('a', href=True):
			連結列表.append(a['href'])
			href = a['href']

		post_content = entry.select('.date')[0].text + " " + entry.select('.author')[0].text + " " + entry.select('.title')[0].text
		post_list.append(post_content)
		清單列表.append({'href':href, 'content':post_content})

def showList():
	i = 1
	for list_content in 清單列表:
		print(i, ' : ', list_content['content'].encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
		i = i+1

	print("程式預設編碼 : ",sys.getdefaultencoding(), ", cmd預設編碼 : ",sys.stdin.encoding)

freshList()
showList()

input_test = ""
check_word = "exit"
while input_test != check_word:
	n = len(清單列表)
	input_test = inputWhich()
	if input_test.isdigit():
		index = int(input_test)-1
		if index < len(清單列表) and -1 < index:
			清單上的內容 = 清單列表[index]
			if "" != 清單上的內容['href']:
				res = rs.get(ptt_domain + 清單上的內容['href'], verify=False)
				soup = BeautifulSoup(res.text)
				text = soup.find('div', id='main-content')
				text = '\n'.join(text.findAll(text=True)).strip();
				print(text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
		else:
			print("error : ", index , len(連結列表))

	if input_test == "list":
		showList()

	if input_test == "refresh":
		post_list = []
		連結列表 = []
		freshList()
		showList()
	
