import sqlite3
import os


dirname=os.path.dirname(__file__)
os.chdir(dirname)

connection = sqlite3.connect("base.db")
cursor = connection.cursor() 
cursor.execute("CREATE TABLE IF NOT EXISTS tab_2(ID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password INTEGER)")

pipls = (("admin","12345"),("user_1","54321"))

cursor.executemany("INSERT INTO tab_2 (username, password) VALUES (?, ?)", pipls)


connection.commit() 	# закрываем транзакцию

connection.close() 	#закрываем соединение с БД