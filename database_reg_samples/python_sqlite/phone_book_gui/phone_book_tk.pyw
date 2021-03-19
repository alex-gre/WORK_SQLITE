from tkinter import ttk
import tkinter as tk
import sqlite3


def connect():
    conn = sqlite3.connect("TELBOOK.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS profile(id INTEGER PRIMARY KEY,\
                              First TEXT, Surname TEXT,Tel TEXT,info TEXT)")
    conn.commit()
    conn.close()


def View():
    conn = sqlite3.connect("TELBOOK.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM profile")
    rows = cur.fetchall()
    for row in rows:
        print(row) # it print all records in the database
        tree.insert("", tk.END, values=row)
    conn.close()


connect()  #  this to create the db

# WIINDOW CREATE======
root = tk.Tk()
root.geometry("1000x500")

# HEADERS DATA============================================================================= 
tree= ttk.Treeview(root, column=("column1", "column2", "column3","column4","column5"), show='headings')
tree.heading("#1", text="NUMBER")
tree.heading("#2", text="FIRST NAME")
tree.heading("#3", text="SURNAME")
tree.heading("#4", text="TELEPHON")
tree.heading("#5", text="INFORMATION")
tree.pack()

# BUTTON CREATE========================== 
b2 = tk.Button(text="view data", command=View)
b2.pack()

root.mainloop()

