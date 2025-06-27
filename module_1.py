from tkinter import END, DISABLED, NORMAL
from tkinter import *
from tkinter import Toplevel
import datetime
import hashlib

def dark(tk, options, color, R1, R2, lang, C1, C2, L_iid, L_sn, L_n, L_mn, L_db, L_s):
    
    tk["bg"] = "#212324"

    L_iid["bg"] = "#212324"
    L_iid["fg"] = "#F1F1F1"
    L_sn["bg"] = "#212324"
    L_sn["fg"] = "#F1F1F1"
    L_n["bg"] = "#212324"
    L_n["fg"] = "#F1F1F1"
    L_mn["bg"] = "#212324"
    L_mn["fg"] = "#F1F1F1"
    L_db["bg"] = "#212324"
    L_db["fg"] = "#F1F1F1"
    L_s["bg"] = "#212324"
    L_s["fg"] = "#F1F1F1"

    options["bg"] = "#212324"

    color["bg"] = "#212324"
    color["fg"] = "#F1F1F1"
    R1["bg"] = "#212324"
    R1["fg"] = "#F1F1F1"
    R2["bg"] = "#212324"
    R2["fg"] = "#F1F1F1"

    lang["bg"] = "#212324"
    lang["fg"] = "#F1F1F1"
    C1["bg"] = "#212324"
    C1["fg"] = "#F1F1F1"
    C2["bg"] = "#212324"
    C2["fg"] = "#F1F1F1"

def light(tk, options, color, R1, R2, lang, C1, C2, L_iid, L_sn, L_n, L_mn, L_db, L_s):

    tk["bg"] = "#F1F1F1"

    L_iid["bg"] = "#F1F1F1"
    L_iid["fg"] = "#212324"
    L_sn["bg"] = "#F1F1F1"
    L_sn["fg"] = "#212324"
    L_n["bg"] = "#F1F1F1"
    L_n["fg"] = "#212324"
    L_mn["bg"] = "#F1F1F1"
    L_mn["fg"] = "#212324"
    L_db["bg"] = "#F1F1F1"
    L_db["fg"] = "#212324"
    L_s["bg"] = "#F1F1F1"
    L_s["fg"] = "#212324"

    options["bg"] = "#F1F1F1"

    color["bg"] = "#F1F1F1"
    color["fg"] = "#212324"
    R1["bg"] = "#F1F1F1"
    R1["fg"] = "#212324"
    R2["bg"] = "#F1F1F1"
    R2["fg"] = "#212324"

    lang["bg"] = "#F1F1F1"
    lang["fg"] = "#212324"
    C1["bg"] = "#F1F1F1"
    C1["fg"] = "#212324"
    C2["bg"] = "#F1F1F1"
    C2["fg"] = "#212324"

def eng(options, color, R1, R2, lang, C1, C2):
    options.title("Options")
    color.config(text = "Color theme:")
    R1.config(text = "Light")
    R2.config(text = "Dark")
    lang.config(text = "Language:")
    C1.config(text = "Russian")
    C2.config(text = "English")

def ru(options, color, R1, R2, lang, C1, C2):
    options.title("Настройки")
    color.config(text = "Цветовая тема:")
    R1.config(text = "Светлая")
    R2.config(text = "Темная")
    lang.config(text = "Язык:")
    C1.config(text = "Русский")
    C2.config(text = "Английский")

def options(tk, L_iid, L_sn, L_n, L_mn, L_db, L_s):
    options = Toplevel()
    options.title("Настройки")
    options.geometry("550x450+960+50")
    options.resizable(False, False)

    color = Label(options, text="Цветовая тема:", font="Arial, 20", anchor="w")
    var = IntVar()
    var.set(0)
    R1 = Radiobutton(options, text="Светлая", font="Arial, 15", value=0, variable = var, command = lambda: light(tk, options, color, R1, R2, lang, C1, C2, L_iid, L_sn, L_n, L_mn, L_db, L_s))
    R2 = Radiobutton(options, text="Темная", font="Arial, 15", value=1, variable = var, command = lambda: dark(tk, options, color, R1, R2, lang, C1, C2, L_iid, L_sn, L_n, L_mn, L_db, L_s))

    color.place(x=20,y=40)
    R1.place(x=20,y=90)
    R2.place(x=130,y=90)
    
    lang = Label(options, text="Язык:", font="Arial, 20", anchor="w")
    varr = IntVar()
    varr.set(0)
    C1 = Checkbutton(options, text="Русский", font="Arial, 15", onvalue=0, variable=varr, command = lambda:ru(options, color, R1, R2, lang, C1, C2))
    C2 = Checkbutton(options, text="Английский", font="Arial, 15", onvalue=1, variable=varr, command = lambda:eng(options, color, R1, R2, lang, C1, C2))

    lang.place(x=20,y=140)
    C1.place(x=20, y=180)
    C2.place(x=130, y=180)

    

def about():
    about = Tk()
    about.title("О программе")
    about.geometry("350x300+960+50")
    about.resizable(False, False)

    L1 = Label(about, text="Разработчик: Романенко Д.", font="Arial, 14", anchor="w")
    L2 = Label(about, text="Версия: 0.1", font="Arial, 14", anchor="w")
    L3 = Label(about, text="Дата: 26.06.2025", font="Arial, 14", anchor="w")
    L4 = Label(about, text="ОС: Windows 10", font="Arial, 14", anchor="w")
    L5 = Label(about, text="ИС Студенты", font="Arial, 20", anchor="w")

    L5.place(x=85, y=50)
    L1.place(x=50, y=110)
    L2.place(x=50, y=140)
    L3.place(x=50, y=170)
    L4.place(x=50, y=200)
    
def documentary():
    doc = Tk()
    doc.title("Документация")
    doc.geometry("350x220+960+50")
    doc.resizable(False, False)
    
    L1 = Label(doc, text="Представьте, что тут", font="Arial, 19")
    L2 = Label(doc, text="супер крутая документация", font="Arial, 19")
    L3 = Label(doc, text="для супер крутой ИС", font="Arial, 19")

    L1.place(x=45, y=50)
    L2.place(x=10, y=85)
    L3.place(x=45, y=120)


def administration(ttk, sqlite3, connection, cursor, log_file):

    tkk = Toplevel()
    tkk.title("Администрирование")
    tkk.geometry("700x570+960+50")
    tkk.resizable(False, False)

    columns_tuple = ("ID", "username")
    tree = ttk.Treeview(tkk, columns= columns_tuple, show="headings")

    tree.heading("ID", text = "ID пользователя", anchor = "w")
    tree.heading("username", text = "Имя пользователя", anchor = "w")

    tree.column("ID", width = 40)
    tree.column("username", width = 70)


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
    
    B_ed = Button(tkk, text="Изменить", font = 'Arial, 13', command = lambda: admin_edit(tree, L_iid, E_username, E_password, B_ed, B_del, B_add, cursor, connection, log_file))
    B_add = Button(tkk, text="Ввести", font = 'Arial, 13', command = lambda: admin_add(tree, E_username, E_password, cursor, connection, log_file))
    B_del = Button(tkk, text="Удалить", font = 'Arial, 13', command = lambda: admin_del(tree, cursor, connection, log_file))
    
    SB = Scrollbar(tkk, orient = VERTICAL, command = tree.yview)
    
    L_iid.place(x=450, y=15, width=80, height=40)
    L_username.place(x=450, y=40, width=170, height=40)
    L_password.place(x=450, y=95, width=170, height=40)
    
    E_username.place(x=453, y=75, width=220, height=25)
    E_password.place(x=453, y=128, width=220, height=25)
    
    B_ed.place(x=470, y=215, width=190, height=40)
    B_add.place(x=470, y=170, width=190, height=40)
    B_del.place(x=470, y=260, width=190, height=40)
    
    SB.place(x = 430, y = 10, height = 530)
    
    tree.configure(yscrollcommand = SB.set)
                  
    tkk.mainloop()

def admin_add(tree, E_username, E_password, cursor, connection, log_file):
    username = E_username.get()
    password = E_password.get()

    password = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute("INSERT INTO tab_2 (username, password) VALUES (?, ?)", (username, password))
    connection.commit()

    for i in tree.get_children():
        tree.delete(i) 

    cursor.execute("SELECT * FROM tab_2")
    users = cursor.fetchall()
    connection.commit()
    
    for d in users:
        tree.insert('', END, values = d)    
    
    now=datetime.datetime.now()
    name = now.strftime("%d.%m.%Y_%H.%M.%S")
    log_file.write(f"{name} Новый пользователь добавлен\n")
        
    E_username.delete(0, END)
    E_password.delete(0, END)
    
def admin_del(tree, cursor, connection, log_file):
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

    now=datetime.datetime.now()
    name = now.strftime("%d.%m.%Y_%H.%M.%S")
    log_file.write(f"{name} Пользователь {id} удален\n")

def admin_edit(tree, L_iid, E_username, E_password, B_ed, B_del, B_add, cursor, connection, log_file):
    global id

    iid = tree.selection()
    
    id = tree.item(iid)["values"][0]
    username = tree.item(iid)["values"][1]
    password = tree.item(iid)["values"][2]

    c = f'IID: {id}'

    L_iid.config(text=c)

    E_username.insert(0, username)
    
    B_ed.config(state=DISABLED)
    B_add.config(text = "Сохранить", command = lambda: admin_save(tree, E_username, E_password, B_add, B_del, B_ed, L_iid, connection, cursor, log_file))
    B_del.config(state=DISABLED)

def admin_save(tree, E_username, E_password, B_add, B_del, B_ed, L_iid, connection, cursor, log_file):
    username = E_username.get()
    password = E_password.get()

    password = hashlib.sha256(password.encode()).hexdigest()
    
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

    now=datetime.datetime.now()
    name = now.strftime("%d.%m.%Y_%H.%M.%S")
    log_file.write(f"{name} Запись пользователя {id} сохранена\n")

    B_del.config(state=NORMAL)
    B_add.config(text="Ввести", command=lambda: admin_add(tree, E_username, E_password, cursor, connection, log_file))
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
    log_file.write(f"{name} Новая запись добавлена\n")
        
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