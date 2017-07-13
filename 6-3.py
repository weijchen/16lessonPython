# -*- coding: utf-8 -*-
# PN: 16 lesson python - word count, Created Mar, 2017
# Version 1.0
# KW: re
# Link: 
# --------------------------------------------------- lib import
import re
# --------------------------------------------------- program
fp = open("sample.txt", "r")
article = fp.read()
new_article = re.sub("[^a-zA-Z\s]", "", article)	#去除不相關符號
words = new_article.split()	# 以空格為分隔符號做切割, then put into a list
print(words)
print()
word_counts = {}

# check whether word exist in word_counts, add one if exist, otherwise add-on with count 1
for word in words:
	if word.upper() in word_counts:
		word_counts[word.upper()] = word_counts[word.upper()] + 1
	else:
		word_counts[word.upper()] = 1
# create a new list to store word_counts' keys, with sorted value
key_list = list(word_counts.keys())
key_list.sort()

# print out key and word_counts[key]
for key in key_list:
	if word_counts[key] > 1:
		print("{}:{}".format(key, word_counts[key]))