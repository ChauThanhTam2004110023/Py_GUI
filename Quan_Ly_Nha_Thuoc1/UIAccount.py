from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import tkinter as tk
import pandas as pd


class UIAccount():
    def __init__(self, username,root) -> None:
        self.root = root
        self.root=username

        self.frame=Frame(root,width=1000,height=900)
        self.frame.configure(bg='grey')

        self.lb_1 = Label(self.frame, text='CẬP NHẬT THÔNG TIN NHÂN VIÊN', fg='blue', font='arail 15 bold')
        self.lb_1.place(x=200, y=20)

        self.lbfram = LabelFrame(self.frame, text='Cập nhật thông tin', font='arail 10 bold',width=850,height=600)
        self.lbfram.place(x = 100 , y = 80)
        # self.lbfram.configure(bg="pink")

        lb_2 = Label( self.lbfram, text='Mã nhân viên (*)', fg='blue', font='arail 10 bold')
        lb_2.place(x=7, y=20)
        self.entry_1 = Entry(self.frame, bd=3, width=30, font='arial 10')
        self.entry_1.place(x=400 ,y=120)

        butt_1 = Button(self.frame, text='Thêm', font='arail 10 bold', width=10,command=self.addData)
        butt_1.place(x=700, y=130)

        button_2 = Button(self.frame, text='Sửa', width=10, font='arail 10 bold', command=self.updateData)
        button_2.place(x=700, y=180)

        button_3 = Button(self.frame, text='Xóa', width=10, font='arail 10 bold', command=self.deleteData)
        button_3.place(x=700, y=230)

        button_3 = Button(self.frame, text='Thoát', width=10, font='arail 10 bold')
        button_3.place(x=700, y=280)

        button_4 = Button(self.frame, text='Tìm kiếm', width=10, font='arail 10 bold', command=self.search_data)
        button_4.place(x=700, y=360)

        self.entry = Entry(self.frame, bd=3, width=30, font='arail 10')
        self.entry.place(x=700, y=390)


        lb_3 = Label(self.frame, text='Họ và tên(*)', fg='blue', font='arail 10 bold')
        lb_3.place(x=120, y=170)
        self.entry_2 = Entry(self.frame, bd=3, width=30, font='arial 10')
        self.entry_2.place(x=400 ,y=170)

        lb_4 = Label(self.frame, text='Ngày Sinh(*)', fg='blue', font='arail 10 bold')
        lb_4.place(x=120, y=220)
        self.entry_3 = Entry(self.frame, bd=3, width=30, font='arial 10')
        self.entry_3.place(x=400 ,y=220)


        lb_4 = Label(self.frame, text='Giới tính(*)', fg='blue' ,font='arail 10 bold')
        lb_4.place(x=120, y=270)
        self.combobox = ttk.Combobox(self.frame, values=['Nam', 'Nữ'], width=10)
        self.combobox.place(x=400, y=270)

        lb_5 = Label(self.frame, text='Địa chỉ(*)', fg='blue', font='arail 10 bold')
        lb_5.place(x=120, y=320)
        self.entry_5 = Entry(self.frame, bd=3, width=30, font='arial 10')
        self.entry_5.place(x=400 ,y=320)

        lb_6 = Label(self.frame, text='Điện thoại(*)', fg='blue', font='arail 10 bold')
        lb_6.place(x=120, y=370)
        self.entry_6 = Entry(self.frame, bd=3, width=30, font='arial 10')
        self.entry_6.place(x=400 ,y=370)

        self.tree=None
        self.loadData()



    def show_selected_row(self,*args):
        self.entry_1.delete(0, END)
        self.entry_2.delete(0, END)
        self.entry_3.delete(0, END)
        self.combobox.delete(0,END)
        self.entry_5.delete(0,END)
        self.entry_6.delete(0, END)

        item = self.tree.focus()
        values = self.tree.item(item, 'values')
        self.entry_1.insert(0, values[0])
        self.entry_2.insert(0, values[1])
        self.entry_3.insert(0, values[2])
        self.combobox.insert(0, values[3])
        self.entry_5.insert(0, values[4])
        self.entry_6.insert(0, values[5])



    def loadData(self):
        self.tree = ttk.Treeview(self.lbfram, show="headings")
        self.tree.place(x=50, y=350, height=130)
        self.tree.bind('<<TreeviewSelect>>', self.show_selected_row)
        path = r"pdas.xlsx"
        df = pd.read_excel(path)

        # df.dropna(how='all', inplace=True)

        cols = df.columns.tolist()

        self.tree.config(columns=cols)
        for i in cols:
            self.tree.column(i, width=100)
        for i in cols:
            self.tree.heading(i, text=i)
        for j in df.values.tolist():
            self.tree.insert('', tk.END, values=j)



    def addData(self):
        ten = self.entry_2.get()
        ngay_sinh = self.entry_3.get()
        gioi_tinh = self.combobox.get()
        dia_chi = self.entry_5.get()
        dien_thoai = self.entry_6.get()

        path = r"pdas.xlsx"
        df = pd.read_excel(path, header=0)

        # Get the current maximum value of the first column
        max_id = df.iloc[:, 0].max()

        # If the maximum value is null, set it to 0
        if pd.isna(max_id):
            max_id = 0

        # Create a new row with the updated ID value
        new_row = [max_id + 1, ten, ngay_sinh, gioi_tinh, dia_chi, dien_thoai]
        df.loc[len(df)] = new_row

        # Save the updated DataFrame to the Excel file
        df.to_excel(path, index=False)

        self.loadData()
        

    
    def updateData(self):
        item = self.tree.focus()
        print(item)
        if not item:
            messagebox.showwarning("Warning", "Hãy chọn 1 hàng để sửa")
            return

        id = int(self.entry_1.get())
        ten = self.entry_2.get()
        ngay_sinh = self.entry_3.get()
        gioi_tinh = self.combobox.get()
        dia_chi = self.entry_5.get()
        dien_thoai = self.entry_6.get()


        df = pd.read_excel('pdas.xlsx')


        # Set the index of the dataframe to be the 'id' column
        df.set_index('Mã nhân viên', inplace=True)

        
        df.loc[id, 'Họ và tên'] = ten
        df.loc[id, 'Ngày sinh'] = ngay_sinh
        df.loc[id, 'Giới tính'] = gioi_tinh
        df.loc[id, 'Địa chỉ'] = dia_chi
        df.loc[id, 'Điện thoại'] = dien_thoai

        # Save the updated dataframe back to the excel file
        df.to_excel('pdas.xlsx', index=True)

        # Reload the data into the treeview
        self.loadData()

    
    def deleteData(self):
        selected_row = self.tree.focus()
        if not selected_row:
            messagebox.showwarning("Error", "Hãy chọn 1 hàng để xóa.")
            return

        # get the values of the selected row
        row_values = self.tree.item(selected_row)['values']


        # load the Excel file as a DataFrame
        path = r"pdas.xlsx"
        df = pd.read_excel(path)
        
        # find the index of the row to delete in the DataFrame
        index_to_delete = df.index[df.iloc[:, 0] == row_values[0]][0]

        # delete the row from the DataFrame and save the changes to the Excel file
        df.drop(index_to_delete, inplace=True)
        df.to_excel(path, index=False)

        # delete the selected row from the Treeview
        # self.tree.delete(selected_row)

        self.loadData()


    def search_data(self):
    # đọc dữ liệu từ file Excel và tìm kiếm dữ liệu

        self.tree = ttk.Treeview(self.lbfram, show="headings")
        self.tree.place(x=50, y=350)
        self.tree.bind('<<TreeviewSelect>>', self.show_selected_row)


        df = pd.read_excel("pdas.xlsx")
        search_value = self.entry.get()
        filtered_df = df[df["Họ và tên"].str.contains(search_value, case=False)]

        cols = df.columns.tolist()

        self.tree.config(columns=cols)
        for i in cols:
            self.tree.column(i, width=100)
        for i in cols:
            self.tree.heading(i, text=i)
    

        # xoá dữ liệu cũ trong treeview
        # for i in self.tree.get_children():
        #     self.tree.delete(i)

        # hiển thị dữ liệu mới trên treeview
        for index, row in filtered_df.iterrows():
            self.tree.insert("", index, values=row.tolist())

        

        df.dropna(how='all', inplace=True)

