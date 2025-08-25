from tkinter import *
from tkinter import ttk
import sqlite3

def add_student():
    r = e_roll.get()
    n = e_name.get()
    e = e_email.get()
    m = e_mobile.get()
    g = c_gender.get()
    d = e_dob.get()
    a = t_address.get("1.0",END)

    conn = sqlite3.connect('student_database.db')
    c = conn.cursor()
    c.execute('INSERT INTO student VALUES(?,?,?,?,?,?,?)',(r,n,e,m,g,d,a))
    conn.commit()
    conn.close()
    show_all()
    clear_all()

def show_all():
    e_search.delete(0,END)
    conn = sqlite3.connect('student_database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM student')
    student_table.delete(*student_table.get_children())
    for r in c:
        student_table.insert("","end",values=r)
    conn.commit()
    conn.close()

def clear_all():
    e_roll.delete(0,END)
    e_name.delete(0,END)
    e_email.delete(0,END)
    e_mobile.delete(0,END)
    e_dob.delete(0,END)
    t_address.delete(1.0,END)
    c_gender.current(0)

def get_data(event):
    current = student_table.item(student_table.focus())
    row = current["values"]

    clear_all()

    e_roll.insert(0,row[0])
    e_name.insert(0,row[1])
    e_email.insert(0,row[2])
    e_mobile.insert(0,row[3])
    e_dob.insert(0,row[5])
    t_address.insert(1.0,row[6])
    c_gender.current(["Female","Male","Other"].index(row[4]))

def update_student():
    e = e_email.get()
    m = e_mobile.get()
    a = t_address.get("1.0",END)
    r = e_roll.get()

    conn = sqlite3.connect('student_database.db')
    c = conn.cursor()
    c.execute('UPDATE student SET email = ?, mobile = ?, address = ? WHERE roll = ?',(e,m,a,r))
    conn.commit()
    conn.close()
    show_all()
    clear_all()

def delete_student():
    r = e_roll.get()

    conn = sqlite3.connect('student_database.db')
    c = conn.cursor()
    c.execute('DELETE FROM student WHERE roll = ?',(r,))
    conn.commit()
    conn.close()
    show_all()
    clear_all()

def search_student():
    s = c_search.get()
    key = e_search.get()

    conn = sqlite3.connect('student_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM student WHERE "+s+" =?",(key,))
    student_table.delete(*student_table.get_children())
    for r in c:
        student_table.insert("","end",values=r)
    conn.commit()
    conn.close()
    


master = Tk()
master.title('Student Management System')
master.geometry('1450x750')

title = Label(master,text="Student Management System",font=("Calibri",40,"bold"), bg="crimson", fg="white", relief=GROOVE)
title.pack(side=TOP, fill=X)

left_frame = Frame(master, bg="crimson", bd=4, relief=RIDGE)
left_frame.place(x=20, y=90, width=550, height=700)

left_frame_title = Label(left_frame, text="Manage Students", font=("Calibri",30,"bold"), bg="white", fg="crimson", bd=4, relief=GROOVE)
left_frame_title.pack(side=TOP,fill=X)

l_roll = Label(left_frame, text="Roll No.", font=("calibri",25,"bold"), fg="white", bg="crimson")
l_roll.place(x=20, y=80)
e_roll = Entry(left_frame,font=("Calibri",18))
e_roll.place(x=200, y=80)

l_name = Label(left_frame, text="Name", font=("calibri",25,"bold"), fg="white", bg="crimson")
l_name.place(x=20, y=130)
e_name = Entry(left_frame,font=("Calibri",18))
e_name.place(x=200, y=130)

l_email = Label(left_frame, text="Email ID", font=("calibri",25,"bold"), fg="white", bg="crimson")
l_email.place(x=20, y=190)
e_email = Entry(left_frame,font=("Calibri",18))
e_email.place(x=200, y=190)

l_mobile = Label(left_frame, text="Mobile No.", font=("calibri",25,"bold"), fg="white", bg="crimson")
l_mobile.place(x=20, y=250)
e_mobile = Entry(left_frame,font=("Calibri",18))
e_mobile.place(x=200, y=250)

l_gender = Label(left_frame, text="Gender", font=("calibri",25,"bold"), fg="white", bg="crimson")
l_gender.place(x=20, y=320)
c_gender = ttk.Combobox(left_frame,font=("calibri",18), width=7, state='readonly')
c_gender["values"]= ("Female","Male","Other")
c_gender.current(0)
c_gender.place(x=150, y=320)

l_dob1 = Label(left_frame, text="DOB", font=("calibri",25,"bold"), fg="white", bg="crimson")
l_dob1.place(x=20, y=370)
l_dob2 = Label(left_frame, text="(DD/MM/YYYY)", font=("calibri",20), fg="white", bg="crimson")
l_dob2.place(x=20, y=410)
e_dob = Entry(left_frame, font=("Calibri",18))
e_dob.place(x=200, y=380)

l_address = Label(left_frame, text="Address", font=("calibri",25,"bold"), fg="white", bg="crimson")
l_address.place(x=20, y=460)
t_address = Text(left_frame,font=("calibri",18), width=20, height = 4)
t_address.place(x=200, y=460)

b_add = Button(left_frame, text="ADD", width=8, height=2, command=add_student)
b_add.place(x=130, y=600)

b_update = Button(left_frame, text="UPDATE", width=8, height=2, command=update_student)
b_update.place(x=230, y=600)

b_delete = Button(left_frame, text="Delete", width=8, height=2, command=delete_student)
b_delete.place(x=330, y=600)

right_frame = Frame(master, bg="crimson", bd=4, relief=RIDGE)
right_frame.place(x=590, y=90, width=960, height=700)

l_search = Label(right_frame, text="Search BY", font=("calibri",25,"bold"), fg="white", bg="crimson")
l_search.place(x=20, y=18)
c_search = ttk.Combobox(right_frame, font=("calibri",15), width=10, state='readonly')
c_search["values"]= ("Roll","Name","Mobile")
c_search.current(0)
c_search.place(x=160, y=27)
e_search =Entry(right_frame,font=("Calibri",18), width=10)
e_search.place(x=290, y= 25)
b_search = Button(right_frame, text="SEARCH",font=("Calibri",20), width=7, command=search_student)
b_search.place(x=430, y=16)
b_showall = Button(right_frame, text="Show All",font=("Calibri",20), width=7, command=show_all)
b_showall.place(x=540, y=16)

table_frame = Frame(right_frame, bg="crimson", bd=4, relief=RIDGE)
table_frame.place(x=20,y=70, width=900, height=600)

hs = Scrollbar(table_frame, orient = HORIZONTAL)
hs.pack(side=BOTTOM, fill=X)
vs = Scrollbar(table_frame, orient=VERTICAL)
vs.pack(side=RIGHT, fill=Y)

student_table = ttk.Treeview(table_frame, columns=("r","n","e","m","g","d","a"),xscrollcommand=hs.set,yscrollcommand=vs.set)
hs.config(command=student_table.xview)
vs.config(command=student_table.yview)
student_table.heading("r",text="Rool No.")
student_table.heading("n",text="Name")
student_table.heading("e",text="Email ID")
student_table.heading("m",text="Mobile No.")
student_table.heading("g",text="Gender")
student_table.heading("d",text="DOB")
student_table.heading("a",text="Address")
student_table["show"]="headings"
student_table.pack(fill=Y, expand=1)
student_table.column("r",width=65)
student_table.column("n",width=170)
student_table.column("e",width=200)
student_table.column("m",width=120)
student_table.column("g",width=75)
student_table.column("d",width=120)
student_table.column("a",width=150)
student_table.bind("<ButtonRelease-1>",get_data)

try:
    conn = sqlite3.connect('student_database.db')
    c = conn.cursor()
    c.execute('CREATE TABLE student (Roll CHAR(3),Name VARCHAR(20),Email VARCHAR(25),Mobile CHAR(10),Gender VARCHAR(10),DOB CHAR(10),Address VARCHAR(50))')
    conn.commit()
    conn.close()
except sqlite3.OperationalError:
    pass

master.mainloop()


