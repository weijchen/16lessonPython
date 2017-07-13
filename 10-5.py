from selenium import webdriver

web = webdriver.Firefox()
web.get('https://facebook.com')
web.quit()