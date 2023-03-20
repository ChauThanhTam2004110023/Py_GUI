from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import tkinter as tk
import pandas as pd



class Type_of_medicine():
    def __init__(self, username, root) -> None:
        self.root = root
        self.username=username
    
        frame = Frame(root, width=1000, height=700)
        self.frame = frame
        self.frame.configure(bg='grey')

        self.lbframe = LabelFrame(self.frame, text="Loại thuốc", font='arail 15 bold', width=900, height=500)
        self.lbframe.place(x=60, y=40)
        # self.lbframe.config(bg='pink')

        lb_1 = Label(self.lbframe, text="Id loại thuốc", font='arail 10', fg='blue')
        lb_1.place(x=50, y=40)
        self.entry_1 = Entry(self.lbframe, bd=3, width=20, font='arail 10')
        self.entry_1.place(x=130, y=40)

        lb_2 = Label(self.lbframe, text="Tên loại thuốc", font='arail 10', fg='blue')
        lb_2.place(x=300, y=40)
        self.entry_2 = Entry(self.lbframe, bd=3, width=20, font='arail 10')
        self.entry_2.place(x=400, y=40)

        lb_3 = Label(self.lbframe, text="Số lượng", font='arail 10', fg='blue')
        lb_3.place(x=50, y=70)
        self.entry_3 = Entry(self.lbframe, bd=3, width=20, font='arail 10')
        self.entry_3.place(x=130, y=70)

        


        butt_1 = Button(self.lbframe, text='Thêm', font='arail 10 bold', width=10, command=self.add_medicine)
        butt_1.place(x=660, y=60)

        butt_2 = Button(self.lbframe, text='Sửa', font='arail 10 bold', width=10, command=self.update_medicine)
        butt_2.place(x=660, y=130)

        butt_3 = Button(self.lbframe, text='Xóa', font='arail 10 bold', width=10, command=self.delete_recours)
        butt_3.place(x=660, y=200)

        self.tree = None
        self.loadData()

    def show_selected_row(self, *args):
        self.entry_1.delete(0, END)
        self.entry_2.delete(0, END)
        self.entry_3.delete(0, END)

        item = self.tree.focus()
        values = self.tree.item(item, 'values')
        self.entry_1.insert(0, values[0])
        self.entry_2.insert(0, values[1])
        self.entry_3.insert(0, values[2])


    def loadData(self):
        self.tree = ttk.Treeview(self.lbframe, show="headings")
        self.tree.place(x=50, y=100, height=130)
        self.tree.bind('<<TreeviewSelect>>', self.show_selected_row)
        path = r"Type_of_medicine.xlsx"
        df = pd.read_excel(path)

        cols = df.columns.tolist()

        self.tree.config(columns=cols)
        for i in cols:
            self.tree.column(i, width=100)
        for i in cols:
            self.tree.heading(i, text=i)
        for j in df.values.tolist():
            self.tree.insert('', tk.END, values=j)


    def add_medicine(self):
        # id = self.entry_1.get()
        name = self.entry_2.get()
        number = self.entry_3.get()

        path = 'Type_of_medicine.xlsx'
        df = pd.read_excel(path, header=0)

        max_id = df.iloc[:, 0].max()

        if pd.isna(max_id):
            max_id = 0

        new_row = [max_id + 1, name, number]
        df.loc[len(df)] = new_row 

        df.to_excel(path, index=False)
        
        self.loadData()


    def update_medicine(self):
        item = self.tree.focus()
        print(item)
        if not item:
            messagebox.showwarning('Hãy chọn môt hàng dữ liệu để cập nhật')
            return
        
        id = int(self.entry_1.get())
        name = self.entry_2.get()
        number = self.entry_3.get()

        df = pd.read_excel('Type_of_medicine.xlsx')


        df.set_index('Id loại thuốc', inplace=True)

        df.loc[id, 'Tên loại thuốc'] = name
        df.loc[id, 'Số lượng'] = number

        df.to_excel('Type_of_medicine.xlsx', index=True)

        self.loadData()



    def delete_recours(self):
        selected_row = self.tree.focus()
        if not selected_row:
            messagebox.showerror("Error", "Hãy chọn 1 hàng để xóa.")
            return

        # get the values of the selected row
        row_values = self.tree.item(selected_row)['values']


        # load the Excel file as a DataFrame
        path = r"Type_of_medicine.xlsx"
        df = pd.read_excel(path)
        
        # find the index of the row to delete in the DataFrame
        index_to_delete = df.index[df.iloc[:, 0] == row_values[0]][0]

        # delete the row from the DataFrame and save the changes to the Excel file
        df.drop(index_to_delete, inplace=True)
        df.to_excel(path, index=False)

        # delete the selected row from the Treeview
        # self.tree.delete(selected_row)

        self.loadData()


