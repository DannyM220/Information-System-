from tkinter import *
from tkinter import ttk
from module_1 import *
import os
import sqlite3
import datetime
 



dirname = os.path.dirname(__file__)
os.chdir(dirname)

if not os.path.exists("log"):
    os.mkdir("log")

now = datetime.datetime.now()
name = now.strftime("%d.%m.%Y_%H.%M.%S")
log_file = open(rf"log\log_{name}.txt", 'w')

if not os.path.exists("info"):
    os.mkdir("info")

tk = Tk()
tk.title("Личные дела студентов")
tk.geometry("900x550+50+50")
tk.resizable(False, False)
tk.protocol("WM_DELETE_WINDOW", lambda: on_closing(log_file, connection, tk))



columns_tuple = ("ID", "surname", "name", "middlename", "dbirth", "speciality")
tree = ttk.Treeview(tk, columns=columns_tuple, show="headings")

tree.heading("ID", text="№ дела", anchor="w", command = lambda: snum_sort(tree))
tree.heading("surname", text="Фамилия", anchor="w", command = lambda: surname_sort(tree))
tree.heading("name", text="Имя", anchor="w")
tree.heading("middlename", text="Отчество", anchor="w")
tree.heading("dbirth", text="Дата рождения", anchor="w")
tree.heading("speciality", text="Специальность", anchor="w")

tree.column("ID", width = 70)
tree.column("surname", width = 130)
tree.column("name", width = 120)
tree.column("middlename", width = 120)
tree.column("dbirth", width = 120)
tree.column("speciality", width = 200)




connection = sqlite3.connect("base.db")
cursor = connection.cursor() 
cursor.execute("SELECT * FROM tab_1")

pipls=cursor.fetchall()
connection.commit()

for data in pipls:
    tree.insert("", END, values=data) 


tree.place(x = 10, y = 10, width = 610, height = 510)


L_iid = Label(tk, text = "IID:", font = 'Arial, 13', anchor = "w")
L_sn = Label(tk, text = "Фамилия:", font = 'Arial, 13')
L_n = Label(tk, text = "Имя:", font = 'Arial, 13')
L_mn = Label(tk, text = "Отчество:", font = 'Arial, 13')
L_db = Label(tk, text = "Дата рождения:", font = 'Arial, 13')
L_s = Label(tk, text = "Специальность:", font = 'Arial, 13')

E_sn = Entry(tk, text="")
E_n = Entry(tk, text="")
E_mn = Entry(tk, text="")
E_db = Entry(tk, text="")
E_s = Entry(tk, text="")

B_ed = Button(tk, text="Изменить", font = 'Arial, 13', command = lambda: edit_data(tree, L_iid, E_sn, E_n, E_mn, E_db, E_s, B_d, B_ed, B_e, B_i, log_file, connection, cursor))
B_d = Button(tk, text="Удалить", font = 'Arial, 13', command = lambda: del_data(tree, log_file, connection, cursor))
B_e = Button(tk, text="Ввести", font = 'Arial, 13', command = lambda: add_data(tree, E_sn, E_n, E_mn, E_db, E_s, log_file, connection, cursor))
B_i = Button(tk, text="Справка", font = 'Arial, 13', command = lambda: get_info(L_iid, E_sn, E_n, E_mn, E_db, E_s))


SB = Scrollbar(tk, orient = VERTICAL, command = tree.yview)
SB2 = Scrollbar(tk, orient = HORIZONTAL, command = tree.xview)

tree.configure(yscrollcommand = SB.set)
tree.configure(xscrollcommand = SB2.set)

L_iid.place(x=643, y=20, width=80, height=40)
L_sn.place(x=624, y=45, width=120, height=40)
L_n.place(x=635, y=100, width=60, height=40)
L_mn.place(x=625, y=155, width=120, height=40)
L_db.place(x=634, y=210, width=150, height=40)
L_s.place(x=619, y=265, width=180, height=40)

E_sn.place(x=647, y=80, width=220, height=25)
E_n.place(x=647, y=135, width=220, height=25)
E_mn.place(x=647, y=190, width=220, height=25)
E_db.place(x=647, y=245, width=220, height=25)
E_s.place(x=647, y=300, width=220, height=25)

B_e.place(x=656, y=345, width=200, height=40)
B_ed.place(x=656, y=390, width=200, height=40)
B_d.place(x=656, y=435, width=200, height=40)
B_i.place(x=656, y=480, width=200, height=40)



SB.place(x = 620, y = 10, height = 510)
SB2.place(x = 10, y = 520, width = 610)


M = Menu()
M1 = Menu(M, tearoff = 0)

M.add_cascade(label = "Файл", menu = M1)

M1.add_command(label = "Настройки") ##, command = setup
M1.add_command(label = "Администрирование", command = lambda: administration(ttk, sqlite3, connection, cursor))
M1.add_command(label = "Создать справку")
M1.add_command(label = "Выход", command = tk.quit)

M2 = Menu(M, tearoff = 0)
M.add_cascade(label = "Сведения", menu = M2)
M2.add_command(label = "О программе")
M2.add_command(label = "Документация")


tk.config(menu=M)

tk.mainloop()