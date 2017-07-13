# -*- coding: utf-8 -*-
# PN: 16 lesson python - input(), Created Feb, 2017
# Version 1.0
# KW: input()
# Link: 
# --------------------------------------------------- lib import
from selenium import webdriver

urls = [
'http://hophd.com',
'http://drho.club.com',
'http://skynetbooks.com',
'http://drho.tw/fit',
'http://drho.tw/news']

web = webdriver.Firefox()
web.set_window_position(0, 0)
web.set_window_size(800, 600)
i = 0
for url in urls:
	web.get(url)
	web.save_screenshot('webpage{}.png'.format(i))
	i += 1
web.quit()