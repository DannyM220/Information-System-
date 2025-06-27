import sqlite3
import os
import hashlib

def hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

dirname=os.path.dirname(__file__)
os.chdir(dirname)

connection = sqlite3.connect("base.db")
cursor = connection.cursor() 
cursor.execute("CREATE TABLE IF NOT EXISTS tab_2(ID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, user_group TEXT)")

pipls = (("admin","12345","Администратор"),("user_1","54321","Пользователь"))

hashed_pipls=[]
for i in pipls:
    hashed_pipls.append((i[0], hash(i[1]), i[2]))

cursor.executemany("INSERT INTO tab_2 (username, password, user_group) VALUES (?, ?, ?)", hashed_pipls)


connection.commit() 	# закрываем транзакцию

connection.close() 	#закрываем соединение с БД