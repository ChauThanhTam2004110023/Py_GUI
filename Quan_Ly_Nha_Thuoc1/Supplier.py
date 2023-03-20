from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import pandas as pd
import tkinter as tk



class Supplier():
    def __init__(self, username, root) -> None:
        self.username = username
        self.root = root

        self.frame = Frame(root, width=1000, height=600)
        self.frame.configure(bg='grey')


        self.lbframe = LabelFrame(self.frame, text='Nhà cung cấp', font='arail 15 bold', width=900, height=500)
        self.lbframe.place(x=60, y=40)
        # self.lbframe.config(bg='grey')

        lb_1 = Label(self.lbframe, text="id(*)", font="arail 10", fg='blue')
        lb_1.place(x=50, y=40)
        self.entry_1 = Entry(self.lbframe, bd=3, width=20, font='arail 10')
        self.entry_1.place(x=100, y=40)

        lb_2 = Label(self.lbframe, text='name(*)', font='arail 10', fg='blue')
        lb_2.place(x=320, y=40)
        self.entry_2 = Entry(self.lbframe, bd=3, width=20, font='arail 10')
        self.entry_2.place(x=380, y=40)

        lb_3 = Label(self.lbframe, text="địa chỉ(*)", font="arail 10", fg='blue')
        lb_3.place(x=50, y=80)
        self.entry_3 = Entry(self.lbframe, bd=3, width=20, font='arail 10')
        self.entry_3.place(x=120, y=80)

        lb_4 = Label(self.lbframe, text="SĐT(*)", font="arail 10", fg='blue')
        lb_4.place(x=320, y=80)
        self.entry_4 = Entry(self.lbframe, bd=3, width=20, font='arail 10')
        self.entry_4.place(x=380, y=80)

        butt_1 = Button(self.lbframe, text='Thêm', font='arail 10 bold', width=10, command=self.addData)
        butt_1.place(x=660, y=60)

        butt_2 = Button(self.lbframe, text='Xóa', font='arail 10 bold', width=10, command=self.removeData)
        butt_2.place(x=660, y=130)

        butt_3 = Button(self.lbframe, text='Sửa', font='arail 10 bold', width=10, command=self.updateData)
        butt_3.place(x=660, y=200)

        self.tree = None
        self.loadData()


    def show_selected_row(self, *args):
        self.entry_1.delete(0, END)
        self.entry_2.delete(0, END)
        self.entry_3.delete(0, END)
        self.entry_4.delete(0, END)

        item = self.tree.focus()
        values = self.tree.item(item, 'values')
        self.entry_1.insert(0, values[0])
        self.entry_2.insert(0, values[1])
        self.entry_3.insert(0, values[2])
        self.entry_4.insert(0, values[3])



    def loadData(self):
        self.tree = ttk.Treeview(self.lbframe, show="headings")
        self.tree.place(x=50, y=150, height=130)
        self.tree.bind('<<TreeviewSelect>>', self.show_selected_row)
        path = r'Supplier.xlsx'
        df = pd.read_excel(path)

        cols = df.columns.tolist()

        self.tree.config(columns=cols)
        for i in cols:
            self.tree.column(i, width=100)
        for i in cols:
            self.tree.heading(i, text=i)
        for j in df.values.tolist():
            self.tree.insert('', tk.END, values=j)


    def addData(self):
        # id = self.entry_1.get()
        name = self.entry_2.get()
        dia_chi = self.entry_3.get()
        sdt = self.entry_4.get()

        path = r'Supplier.xlsx'
        df = pd.read_excel(path, header=0)

        max_id = df.iloc[:, 0].max()

        if pd.isna(max_id):
            max_id = 0

        new_row = [max_id + 1, name, dia_chi, sdt]
        df.loc[len(df)] = new_row

        df.to_excel(path, index=False)
        self.loadData()

    def updateData(self):
        item = self.tree.focus()
        if not item:
            messagebox.showwarning('Chọn một dòng dữ liệu để cập nhật')
            return
        
        id = int(self.entry_1.get())
        name = self.entry_2.get()
        froms = self.entry_3.get()
        phone = self.entry_4.get()

        df = pd.read_excel('Supplier.xlsx')

        df.set_index('id', inplace=True)
        df.loc[id, ['name']] = name
        df.loc[id, ['địa chỉ']] = froms
        df.loc[id, ['SĐT']] = phone

        df.to_excel('Supplier.xlsx', index=True)
        self.loadData()


    def removeData(self):
        selected_row = self.tree.focus()
        if not selected_row:
            messagebox.showwarning('Chọn một dòng dữ liệu để xóa.')
            return
        
        row_values = self.tree.item(selected_row)['values']

        path = 'Supplier.xlsx'
        df = pd.read_excel(path)

        index_to_delete = df.index[df.iloc[:, 0] == row_values[0]]

        df.drop(index_to_delete, inplace=True)
        df.to_excel(path, index=False)

        self.loadData()


    

    

