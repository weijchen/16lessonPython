# -*- coding: utf-8 -*-
# PN: SQLite practice(Students' info database), Created Feb, 2017
# Version 1.0
# KW: student db, append, edit, delete, display
# Link: 
# --------------------------------------------------- lib import
import sqlite3
conn = sqlite3.connect('scores.sqlite')
# ------------------------------------------------------------- start
def disp_menu():
	print("學生資料編輯")
	print("-----------------")
	print("1. 新增")
	print("2. 編輯")
	print("3. 刪除")
	print("4. 顯示所有學生")
	print("0. 結束")
	print("-----------------")

def append_data():
	while True:
		no = int(input("請輸入學生座號 (-1停止輸入):"))
		if no == -1:
			break
		name = input("請輸入學生姓名:")
		sqlstr = "select * from student where stdno={};".format(no)
		cursor = conn.execute(sqlstr)
		if len(cursor.fetchall()) > 0:
			print('所輸入的座號已經有資料')
		else:
			sqlstr = "insert into student values({}, '{}');".format(no, name)
			conn.execute(sqlstr)
			conn.commit()

def edit_data():
	no = input("請輸入要編輯的學生座號")
	sqlstr = "select * from student where stdno={};".format(no)
	cursor = conn.execute(sqlstr)
	rows = cursor.fetchall()
	if len(rows) > 0:
		print("目前的學生姓名: ", row[0][1])
		name = input("請輸入學生姓名:")
		sqlstr = "update student set name='{}' where stdno={};".format(name, no)
		conn.execute(sqlstr)
		conn.commit()
	else:
		print("找不到要編輯的學生座號")

def del_data():
	no = input("請輸入要刪除的學生座號")
	sqlstr = "select * from student where stdno={};".format(no)
	cursor = conn.execute(sqlstr)
	rows = cursor.fetchall()
	if len(rows) > 0:
		print("確定要刪除座號 {} 的 {} ?".format(rows[0][0], rows[0][1]))
		answer = input("確定要刪除嘛? (y/n)")
		if answer == 'y' or answer == 'Y':
			sqlstr = "delete from student where stdno={};".format(no)
			conn.execute(sqlstr)
			conn.commit()
			print("已刪除指定學生")
		else:
			print("已取消")
	else:
		print("找不到此座號")

def disp_data():
	cursor = conn.execute('select * from student;')
	for row in cursor:
		print("No {}: {}".format(row[0], row[1]))
# -------------------------------------------------------------
while True:
	disp_menu()
	choice = int(input("請輸入指令:"))
	if choice == 0:
		break
	elif choice == 1:
		append_data()
	elif choice == 2:
		edit_data()
	elif choice == 3:
		del_data()
	elif choice == 4:
		disp_data()
	else:
		break
	x = input("Press Enter to return")
