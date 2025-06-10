from msilib.schema import ComboBox
from tkinter import END, DISABLED, NORMAL
from tkinter import *
import datetime

def options():
    options = Tk()
    options.title("Настройки")
    options.geometry("550x450+960+50")
    options.resizable(False, False)

    L1 = Label(options, text = "Язык", font = "Arial, 14", anchor = "w")
    L2 = Label(options, text = "Тема", font = "Arial, 14", anchor = "w")
    R1 = Radiobutton(options, text = "Темная", anchor = "w")
    R2 = Radiobutton(options, text = "Светлая", anchor = "w")
    Cb1 = ComboBox(options)


def administration(ttk, sqlite3, connection, cursor):

    tkk = Tk()
    tkk.title("Администрирование")
    tkk.geometry("700x570+960+50")
    tkk.resizable(False, False)

    columns_tuple = ("ID", "username", "password")
    tree = ttk.Treeview(tkk, columns= columns_tuple, show="headings")

    tree.heading("ID", text = "ID пользователя", anchor = "w")
    tree.heading("username", text = "Имя пользователя", anchor = "w")
    tree.heading("password", text = "Пароль", anchor = "w")

    tree.column("ID", width = 40)
    tree.column("username", width = 70)
    tree.column("password", width = 50)


    connection = sqlite3.connect("base.db")
    cursor = connection.cursor() 
    cursor.execute("SELECT * FROM tab_2")

    users=cursor.fetchall()
    connection.commit()

    for data in users:
        tree.insert("", END, values=data) 

    
    tree.place(x = 10,y = 10, width = 420, height = 530)
    
    L_iid = Label(tkk, text = "IID:", font = 'Arial, 13', anchor = "w")
    L_username = Label(tkk, text = "Имя пользователя:", font = 'Arial, 13', anchor = "w")
    L_password = Label(tkk, text = "Пароль:", font = 'Arial, 13', anchor = "w")
    
    E_username = Entry(tkk, text="")
    E_password = Entry(tkk, text="")
    
    B_ed = Button(tkk, text="Изменить", font = 'Arial, 13', command = lambda: admin_edit(tree, L_iid, E_username, E_password, B_ed, B_del, B_add, B_bl, cursor, connection))
    B_add = Button(tkk, text="Ввести", font = 'Arial, 13', command = lambda: admin_add(tree, E_username, E_password, cursor, connection))
    B_del = Button(tkk, text="Удалить", font = 'Arial, 13', command = lambda: admin_del(tree, cursor, connection))
    B_bl = Button(tkk, text="Блокировать", font = 'Arial, 13')
    
    SB = Scrollbar(tkk, orient = VERTICAL, command = tree.yview)
    
    L_iid.place(x=450, y=15, width=80, height=40)
    L_username.place(x=450, y=40, width=170, height=40)
    L_password.place(x=450, y=95, width=170, height=40)
    
    E_username.place(x=453, y=75, width=220, height=25)
    E_password.place(x=453, y=128, width=220, height=25)
    
    B_ed.place(x=470, y=215, width=190, height=40)
    B_add.place(x=470, y=170, width=190, height=40)
    B_del.place(x=470, y=260, width=190, height=40)
    B_bl.place(x=470, y=305, width=190, height=40)
    
    SB.place(x = 430, y = 10, height = 530)
    
    tree.configure(yscrollcommand = SB.set)
                  
    tkk.mainloop()

def admin_add(tree, E_username, E_password, cursor, connection):
    username = E_username.get()
    password = E_password.get()

    cursor.execute("INSERT INTO tab_2 (username, password) VALUES (?, ?)", (username, password))
    connection.commit()

    for i in tree.get_children():
        tree.delete(i) 

    cursor.execute("SELECT * FROM tab_2")
    users = cursor.fetchall()
    connection.commit()
    
    for d in users:
        tree.insert('', END, values = d)    
    
    # now=datetime.datetime.now()
    # name = now.strftime("%d.%m.%Y_%H.%M.%S")
    # log_file.write(f"{name} Запись {id} добавлена\n")
        
    E_username.delete(0, END)
    E_password.delete(0, END)
    
def admin_del(tree, cursor, connection):
    data = tree.item(tree.selection())
    data_ID = data["values"][0]
    cursor.execute(f"DELETE FROM tab_2 WHERE id={data_ID}")
    connection.commit()

    for item in tree.get_children():
        tree.delete(item)
    cursor.execute("SELECT * FROM tab_2")
    pipls = cursor.fetchall()
    connection.commit()    
    for d in pipls:
        tree.insert('', END, values=d)

    # now=datetime.datetime.now()
    # name = now.strftime("%d.%m.%Y_%H.%M.%S")
    # log_file.write(f"{name} Запись {id} удалена\n")

def admin_edit(tree, L_iid, E_username, E_password, B_ed, B_del, B_add, B_bl, cursor, connection):
    global id

    iid = tree.selection()
    
    id = tree.item(iid)["values"][0]
    username = tree.item(iid)["values"][1]
    password = tree.item(iid)["values"][2]

    c = f'IID: {id}'

    L_iid.config(text=c)

    E_username.insert(0, username)
    E_password.insert(0, password)
    
    B_ed.config(state=DISABLED)
    B_add.config(text = "Сохранить", command = lambda: admin_save(tree, E_username, E_password, B_add, B_del, B_bl, B_ed, L_iid, connection, cursor))
    B_del.config(state=DISABLED)
    B_bl.config(state=DISABLED)

def admin_save(tree, E_username, E_password, B_add, B_del, B_bl, B_ed, L_iid, connection, cursor):
    username = E_username.get()
    password = E_password.get()
    
    cursor.execute("UPDATE tab_2 SET username=?, password=? WHERE id=?", (username, password, id))
    connection.commit()

    for item in tree.get_children():
        tree.delete(item)
    cursor.execute("SELECT * FROM tab_2")
    pipls = cursor.fetchall()
    connection.commit()    
    for d in pipls:
        tree.insert('', END, values=d)
        
    E_username.delete(0, END)
    E_password.delete(0, END)

    B_del.config(state=NORMAL)
    B_bl.config(state=NORMAL)
    B_add.config(text="Ввести", command=lambda: admin_add(tree, E_username, E_password, cursor, connection))
    B_ed.config(state=NORMAL)
    L_iid.config(text="IID: ")

def on_closing(log_file, connection, tk):
    now = datetime.datetime.now()
    name = now.strftime("%d.%m.%Y_%H.%M.%S")
    log_file.write(f"{name} Выключение ИС")
    log_file.close()
    connection.close()
    tk.destroy()


def save_data(tree, L_iid, E_sn, E_n, E_mn, E_db, E_s, B_d, B_ed, B_e, B_i, cursor, connection, log_file):
        
    surname = E_sn.get()
    name = E_n.get()
    middlename = E_mn.get()
    dbirth = E_db.get()
    speciality = E_s.get()
    
    cursor.execute("UPDATE tab_1 SET surname=?, name=?, middlename=?, dbirth=?, speciality=? WHERE id=?", (surname, name, middlename, dbirth, speciality, id))
    connection.commit()

    for item in tree.get_children():
        tree.delete(item)
    cursor.execute("SELECT * FROM tab_1")
    pipls = cursor.fetchall()
    connection.commit()    
    for d in pipls:
        tree.insert('', END, values=d)
        
    E_sn.delete(0, END)
    E_n.delete(0, END)
    E_mn.delete(0, END)
    E_db.delete(0, END)
    E_s.delete(0, END)

    B_d.config(state=NORMAL)
    B_ed.config(state=NORMAL)
    B_i.config(state=NORMAL)
    B_e.config(text="Ввод", command=lambda:  add_data(tree, E_sn, E_n, E_mn, E_db, E_s, log_file, connection, cursor))
    L_iid.config(text="IID: ")

    now=datetime.datetime.now()
    name = now.strftime("%d.%m.%Y_%H.%M.%S")
    log_file.write(f"{name} Запись {id} изменена\n")

def edit_data(tree, L_iid, E_sn, E_n, E_mn, E_db, E_s, B_d, B_ed, B_e, B_i, log_file, connection, cursor):
    global id

    iid = tree.selection()
    
    id = tree.item(iid)["values"][0]
    surname = tree.item(iid)["values"][1]
    name = tree.item(iid)["values"][2]
    middlename = tree.item(iid)["values"][3]
    dbirth = tree.item(iid)["values"][4]
    speciality = tree.item(iid)["values"][5]

    c = f'IID: {id}'

    L_iid.config(text=c)

    E_sn.insert(0,surname)
    E_n.insert(0, name)
    E_mn.insert(0, middlename)
    E_db.insert(0, dbirth)
    E_s.insert(0, speciality)

    B_d.config(state=DISABLED)
    B_ed.config(state=DISABLED)
    B_i.config(state=DISABLED)
    B_e.config(text="Сохранить", command=lambda: save_data(tree, L_iid, E_sn, E_n, E_mn, E_db, E_s, B_d, B_ed, B_e, B_i, cursor, connection, log_file))

def del_data(tree, log_file, connection, cursor):
    data = tree.item(tree.selection())
    data_ID = data["values"][0]
    cursor.execute(f"DELETE FROM tab_1 WHERE id={data_ID}")
    connection.commit()

    for item in tree.get_children():
        tree.delete(item)
    cursor.execute("SELECT * FROM tab_1")
    pipls = cursor.fetchall()
    connection.commit()    
    for d in pipls:
        tree.insert('', END, values=d)

    now=datetime.datetime.now()
    name = now.strftime("%d.%m.%Y_%H.%M.%S")
    log_file.write(f"{name} Запись {id} удалена\n")

def add_data(tree, E_sn, E_n, E_mn, E_db, E_s, log_file, connection, cursor):

    surname = E_sn.get()
    name = E_n.get()
    middlename = E_mn.get()
    dbirth = E_db.get()
    speciality = E_s.get()

    cursor.execute("INSERT INTO tab_1 (surname, name, middlename, dbirth, speciality) VALUES (?, ?, ?, ?, ?)", (surname, name, middlename, dbirth, speciality))
    connection.commit()

    for i in tree.get_children():
        tree.delete(i) 

    cursor.execute("SELECT * FROM tab_1")
    pipls = cursor.fetchall()
    connection.commit()
    
    for d in pipls:
        tree.insert('', END, values = d)    
    
    
    now=datetime.datetime.now()
    name = now.strftime("%d.%m.%Y_%H.%M.%S")
    log_file.write(f"{name} Запись {id} добавлена\n")
        
    E_sn.delete(0, END)
    E_n.delete(0, END)
    E_mn.delete(0, END)
    E_db.delete(0, END)
    E_s.delete(0, END)

def get_info(connection, cursor):
    cursor.execute("SELECT ID FROM tab_1")
    id_number = cursor.fetchone()
    iid = 1
    info_file = open(rf"info\info_{1}.txt", 'w')
    info_file.write(f" Справка по делу номер {iid}")
    info_file.write(f" Фамилия: {iid}, Имя: {iid}, Отчество: {iid},  Дата рождения: {iid}, Специальность: {iid}")
    info_file.close()


def snum_sort(tree):
    id_tuple = tree.get_children("")
    snum_list=[]

    for iid in id_tuple:
        snum_list.append((tree.item(iid)["values"][0],iid))
    
    snum_list.sort(reverse = False)

    n = len(snum_list)

    for i in range(n):
        tree.move(snum_list[i][1], "", i)

    tree.heading("ID", command = lambda: snum_sort_rev(tree))
def snum_sort_rev(tree):
    id_tuple = tree.get_children("")
    snum_list=[]

    for iid in id_tuple:
        snum_list.append((tree.item(iid)["values"][0],iid))
    
    snum_list.sort(reverse = True)

    n = len(snum_list)

    for i in range(n):
        tree.move(snum_list[i][1], "", i)

    tree.heading("ID", command = lambda: snum_sort(tree))

def surname_sort(tree):
    id_tuple = tree.get_children("")
    surname_list=[]

    for iid in id_tuple:
        surname_list.append((tree.item(iid)["values"][1],iid))
    
    surname_list.sort(reverse = False)

    n = len(surname_list)

    for i in range(n):
        tree.move(surname_list[i][1], "", i)

    tree.heading("surname", command = lambda: surname_sort_rev(tree))
def surname_sort_rev(tree):
    id_tuple = tree.get_children("")
    surname_list=[]

    for iid in id_tuple:
        surname_list.append((tree.item(iid)["values"][1],iid))
    
    surname_list.sort(reverse = True)

    n = len(surname_list)

    for i in range(n):
        tree.move(surname_list[i][1], "", i)

    tree.heading("surname", command = lambda: surname_sort(tree))