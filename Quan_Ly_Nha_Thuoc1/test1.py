from tkinter import *
# import tkinter as tk
from tkinter import ttk

def show_data(event):
    item = treeview.selection()[0]
    data = treeview.item(item, "values")
    label.config(text=data)

root = Tk()
label = Label(root, text="")
label.pack()

treeview = ttk.Treeview(root)
treeview.pack()

treeview["columns"] = ("col1", "col2")
treeview.column("#0", width=100)
treeview.column("col1", width=100)
treeview.column("col2", width=100)

treeview.heading("#0", text="ID")
treeview.heading("col1", text="Name")
treeview.heading("col2", text="Age")

treeview.insert("", "end", text="001", values=("John", "30"))
treeview.insert("", "end", text="002", values=("Mike", "25"))
treeview.insert("", "end", text="003", values=("Lisa", "35"))

treeview.bind("<<TreeviewSelect>>", show_data)

root.mainloop()




