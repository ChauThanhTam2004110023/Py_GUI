import random
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import tkinter as tk
import pandas as pd



class Sales_medicine():
    def __init__(self, username, root):
        
        def change_label_color(label):
        # Tạo một danh sách các màu
            colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
            # Chọn một màu ngẫu nhiên từ danh sách
            color = random.choice(colors)
            # Thay đổi màu chữ của label
            label.config(foreground=color)
            # Gọi lại hàm sau 1 giây
            label.after(1000, change_label_color, label)
        self.username = username
        self.root = root

        self.frame = Frame(root, width=1300, height=900)
        self.frame.configure(bg='grey')

        self.lbfframe = LabelFrame(
            self.frame, text='Mua thuốc', font='arail 15 bold', width=1200, height=600)
        self.lbfframe.place(x=60, y=40)
        # self.lbfframe.configure(bg='pink')
        change_label_color(self.lbfframe)
        lb_1 = Label(self.frame, text='id_thuoc',font='arail 10 bold', fg='blue')
        lb_1.place(x=100, y=70)
        self.entry_1 = Entry(self.frame, bd=3, width=20,font='arail 10')  # id_thuoc
        self.entry_1.place(x=300, y=70)

        lb_NameTable = Label(
            self.frame, text="BẢNG CHỌN THUỐC ĐÃ CHỌN", font="arial 15 bold", fg="purple")
        lb_NameTable.place(x= 650, y =70)

        lb_2 = Label(self.frame, text='Tên thuốc',
                     font='arail 10 bold', fg='blue')
        lb_2.place(x=100, y=100)
        self.entry_2 = Entry(self.frame, bd=3, width=20, font='arail 10')
        self.entry_2.place(x=300, y=100)

        lb_3 = Label(self.frame, text='Số lượng',
                     font='arail 10 bold', fg='blue')
        lb_3.place(x=100, y=130)
        self.entry_3 = Entry(self.frame, bd=3, width=20, font='arail 10')
        self.entry_3.place(x=300, y=130)

        button_add = Button(self.frame, text='Thêm', width=10,
                            font='arail 10 bold', command=self.add_data)
        button_add.place(x=400, y=580)
        


        

        # button_edit = Button(self.frame, text='Sửa', width=10,
        #                      font='arail 10 bold', command=self.edit_data)
        # button_edit.place(x=600, y=580)

        lb_4 = Label(self.frame, text='Giá thuốc',
                     font='arail 10 bold', fg='blue')
        lb_4.place(x=100, y=160)
        self.entry_4 = Entry(self.frame, bd=3, width=20, font='arail 10')
        self.entry_4.place(x=300, y=160)

        lb_5 = Label(self.frame, text='Hàm lượng',
                     font='arail 10 bold', fg='blue')
        lb_5.place(x=100, y=190)
        self.entry_5 = Entry(self.frame, bd=3, width=20, font='arail 10')
        self.entry_5.place(x=300, y=190)

        lb_6 = Label(self.frame, text='Tên khách hàng : ',
                     font='arail 10 bold', fg='blue')
        lb_6.place(x=100, y=250)
        self.combobox_6 = Entry(
            self.frame, bd=3, width=20, font='arail 10')
        self.combobox_6.place(x=300, y=250)
       

        lb_7 = Label(self.frame, text='Số điện thoại',
                     font='arail 10 bold', fg='blue')
        lb_7.place(x=100, y=280)
        self.entry_7 = Entry(self.frame, bd=3, width=20, font='arail 10')
        self.entry_7.place(x=300, y=280)

        lb_8 = Label(self.frame, text='Ngày/tháng/năm mua', font='arail 10 bold', fg='blue')
        lb_8.place(x=100, y=220)
        
        button_accept = Button(self.frame, text='Xác nhận',
                               font='arail 10 bold', command=self.add_data)
        button_accept.place(x = 650, y=280)


        button_remove = Button(self.frame, text='Xóa', width=10,
                               font='arail 10 bold', command=self.remove_data)
        button_remove.place(x=750, y=280)

        button_remove = Button(self.frame, text='Sửa', width=10,
                               font='arail 10 bold', command=self.edit_data)
        button_remove.place(x=880, y=280)

        self.entry_8 = Entry(self.frame, bd=3, width=20, font='arail 10')
        self.entry_8.place(x=300, y=220)

        button = Button(self.frame, text='Tìm kiếm', width=10,
                        font='arail 10 bold', command=self.search_data)
        button.place(x=100, y=310)

        self.entry = Entry(self.frame, bd=3, width=50, font='arail 10')
        self.entry.place(x=200, y=310)

        # lb_9 = Label(self.frame, text='Tên loại thuốc',
        #              font='arail 10 bold', fg='blue')
        # lb_9.place(x=500, y=150)
        
        # self.combobox_9 = ttk.Combobox(self.frame,  values=['Click'], width=20)
        # self.combobox_9.place(x=600, y=150)
        # self.combobox_9.bind("<<ComboboxSelected>>", self.loadComboboxmedicine)
        self.load_Data_Frame()
        self.tree = None
        self.load_Data()

    def edit_data(self):
        item = self.tree_a.focus()
        print(item)
        if not item:
            messagebox.showwarning("Warning", "Hãy chọn 1 hàng để sửa")
            return

        id = int(self.entry_1.get())
        name_thuoc = self.entry_2.get()
        so_luong = self.entry_3.get()
        gia_thuoc = self.entry_4.get()
        ham_luong = self.entry_5.get()
        ngayMua = self.entry_8.get()
        ten_khach = self.combobox_6.get()
        sdt = self.entry_7.get()
        
        df = pd.read_excel("Sales_medicine.xlsx")

        df.set_index('id_Thuoc', inplace=True)

        df.loc[id, 'so_luong'] = so_luong

        df.loc[id, 'gia_thuoc'] = gia_thuoc

        df.loc[id, 'ham_luong'] = ham_luong

        df.loc[id, 'ngayMua'] = ngayMua

        df.loc[id, 'ten_khach'] = ten_khach

        df.loc[id, 'sdt'] = sdt

        df.loc[id, 'name_Thuoc'] = name_thuoc
        

        df.to_excel('Sales_medicine.xlsx', index=True)
        self.load_Data_Frame()
        self.tree = None
        self.load_Data()
   
        

    # def load_Data_Frame(self):
    #     self.tree = ttk.Treeview(self.lbfframe, show="headings")
    #     self.tree.place(x=60, y=10, height=130)
    #     self.tree.bind('<<TreeviewSelect>>', self.show_selected_row)
    #     path = r"tableTemple.xlsx"
    #     df = pd.read_excel(path)

    #     cols = df.columns.tolist()

    #     self.tree.config(columns=cols)
    #     for i in cols:
    #         self.tree.column(i, width=100)
    #     for i in cols:
    #         self.tree.heading(i, text=i)
    #     for j in df.values.tolist():
    #         self.tree.insert('', tk.END, values=j)

    def loadComboboxmedicine(self, *args):
        path = r'Type_of_medicine.xlsx'
        df = pd.read_excel(path)
        supplier = df.iloc[:, 1].tolist()
        self.combobox_9.config(values=supplier)
        self.load_Data_Frame()
        self.load_Data()

    def loadComboboxValue(self, *args):
        path = r'Supplier.xlsx'
        df = pd.read_excel(path)
        supplier = df.iloc[:, 1].tolist()
        self.combobox_6.config(values=supplier)
        self.load_Data_Frame()
        self.load_Data()

    def show_selected_row(self, *args):
        self.entry_1.delete(0, END)
        self.entry_2.delete(0, END)
        # self.entry_3.delete(0, END)
        self.entry_4.delete(0, END)
        self.entry_5.delete(0, END)
        self.combobox_6.delete(0, END)
        self.entry_7.delete(0, END)
        self.entry_8.delete(0, END)

        item = self.tree.focus()
        values = self.tree.item(item, "values")
        print(values)

        self.entry_1.insert(0, values[0])
        self.entry_2.insert(0, values[1])
        # self.entry_3.insert(0, values[2])
        self.entry_4.insert(0, values[3])
        self.entry_5.insert(0, values[4])
        # self.combobox_6.insert(0, values[5])
        # self.entry_7.insert(0, values[6])
        # self.entry_8.insert(0, values[7])
        # self.load_Data_Frame()
        # self.load_Data()


    def show_selected_row_a(self, *args):
        self.entry_1.delete(0, END)
        self.entry_2.delete(0, END)
        self.entry_3.delete(0, END)
        self.entry_4.delete(0, END)
        self.entry_5.delete(0, END)
        self.combobox_6.delete(0, END)
        self.entry_7.delete(0, END)
        self.entry_8.delete(0, END)

        item = self.tree_a.focus()
        values = self.tree_a.item(item, "values")
        print(values)
        self.entry_1.insert(0, values[0])
        self.entry_2.insert(0, values[1])
        self.entry_3.insert(0, values[2])
        self.entry_4.insert(0, values[3])
        self.entry_5.insert(0, values[4])
        self.entry_8.insert(0, values[5])

        self.combobox_6.insert(0, values[6])
        self.entry_7.insert(0, values[7])
        # self.entry_8.insert(0, values[7])
        # self.load_Data_Frame()
        # self.load_Data()






    def load_Data(self):
        self.tree = ttk.Treeview(self.lbfframe, show="headings")
        self.tree.place(x=50, y=280, height=130)
        self.tree.bind('<<TreeviewSelect>>', self.show_selected_row)
        path = r"medicine.xlsx"
        df = pd.read_excel(path)

        cols = df.columns.tolist()

        self.tree.config(columns=cols)
        for i in cols:
            self.tree.column(i, width=100)
        for i in cols:
            self.tree.heading(i, text=i)
        for j in df.values.tolist():
            self.tree.insert('', tk.END, values=j)
    def load_Data_Frame(self):
        self.tree_a = ttk.Treeview(self.lbfframe, show="headings")
        self.tree_a.place(x=400, y=50, height=130)
        self.tree_a.bind('<<TreeviewSelect>>', self.show_selected_row_a)
        path = r"Sales_medicine.xlsx"
        df = pd.read_excel(path)

        cols = df.columns.tolist()

        self.tree_a.config(columns=cols)
        for i in cols:
            self.tree_a.column(i, width=100)
        for i in cols:
            self.tree_a.heading(i, text=i)
        for j in df.values.tolist():
            self.tree_a.insert('', tk.END, values=j)

    

    def search_data(self):
        # đọc dữ liệu từ file Excel và tìm kiếm dữ liệu

        self.tree = ttk.Treeview(self.lbfframe, show="headings")
        self.tree.place(x=50, y=280)
        self.tree.bind('<<TreeviewSelect>>', self.show_selected_row)

        df = pd.read_excel("tableTemple.xlsx")
        search_value = self.entry.get()
        filtered_df = df[df["name_thuoc"].str.contains(
            search_value, case=False)]

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
        self.load_Data_Frame()
        self.load_Data()

    def add_data(self):
        name_thuoc = self.entry_2.get()
        so_luong = self.entry_3.get()
        gia_thuoc = int(self.entry_4.get()) * int(self.entry_3.get())
        ham_luong = self.entry_5.get()
        ten_khach = self.combobox_6.get()
        sdt = self.entry_7.get()
        ngayMua = self.entry_8.get()

        path = r'Sales_medicine.xlsx'
        df = pd.read_excel(path, header=0)

        max_id = df.iloc[:, 0].max()

        if pd.isna(max_id):
            max_id = 0

        # new_row = [max_id + 1, name_thuoc, so_luong,
        #            gia_thuoc, ham_luong, nha_cung_cap, don_vi, hsd]
        new_row = [max_id + 1, name_thuoc, so_luong,str(gia_thuoc), ham_luong, ngayMua, ten_khach, str(sdt)]
        df.loc[len(df)] = new_row

        df.to_excel(path, index=False)
        
        self.load_Data_Frame()
        self.load_Data()

    def xac_nhan_mua(self):
        name_thuoc = self.entry_2.get()
        so_luong = self.entry_3.get()
        gia_thuoc = int(self.entry_4.get()) * int(self.entry_3.get())
        ham_luong = self.entry_5.get()
        nha_cung_cap = self.combobox_6.get()
        don_vi = self.entry_7.get()
        ngayMua = self.entry_8.get()

        path = r'Sales_medicine.xlsx'
        df = pd.read_excel(path, header=0)

        max_id = df.iloc[:, 0].max()

        if pd.isna(max_id):
            max_id = 0

        # new_row = [max_id + 1, name_thuoc, so_luong,
        #            gia_thuoc, ham_luong, nha_cung_cap, don_vi, hsd]
        new_row = [max_id + 1, name_thuoc, so_luong, str(gia_thuoc), ham_luong, ngayMua]
        df.loc[len(df)] = new_row

        df.to_excel(path, index=False)

        self.load_Data_Frame()
        self.load_Data()

    # def edit_data(self):
    #     item = self.tree.focus()
    #     print(item)
    #     if not item:
    #         messagebox.showwarning("Warning", "Hãy chọn 1 hàng để sửa")
    #         return

    #     id = int(self.entry_1.get())
    #     name_thuoc = self.entry_2.get()
    #     so_luong = self.entry_3.get()
    #     gia_thuoc = self.entry_4.get()
    #     ham_luong = self.entry_5.get()
    #     nha_cung_cap = self.combobox_6.get()
    #     don_vi = self.entry_7.get()
    #     hsd = self.entry_8.get()

    #     df = pd.read_excel("medicine.xlsx")

    #     df.set_index('id_thuoc', inplace=True)

    #     df.loc[id, 'name_thuoc'] = name_thuoc
    #     df.loc[id, 'so_luong'] = so_luong
    #     df.loc[id, 'gia_thuoc'] = gia_thuoc
    #     df.loc[id, 'ham_luong'] = ham_luong
    #     df.loc[id, 'nha_cung_cap'] = nha_cung_cap
    #     df.loc[id, 'don_vi'] = don_vi
    #     df.loc[id, 'HSD'] = hsd

    #     df.to_excel('medicine.xlsx', index=True)

    #     self.load_Data()

    def remove_data(self):
        select_now = self.tree_a.focus()
        if not select_now:
            messagebox.showerror(title="Info" ,message="Hãy chọn 1 hàng để xóa")
            return

        row_values = self.tree_a.item(select_now)['values']
        print(row_values)
        path = r'Sales_medicine.xlsx'
        df = pd.read_excel(path)

        index_to_delete = df.index[df.iloc[:, 0] == row_values[0]][0]

        df.drop(index_to_delete, inplace=True)

        df.to_excel(path, index=False)

        self.load_Data_Frame()
        self.load_Data()



        # select_now = self.tree.focus()
        # if not select_now:
        #     messagebox.showerror(title="Info" ,message="Hãy chọn 1 hàng để xóa")
        #     return

        # row_values = self.tree.item(select_now)['values']

        # path = r'tableTemple.xlsx'
        # df = pd.read_excel(path)

        # index_to_delete = df.index[df.iloc[:, 0] == row_values[0]][0]

        # df.drop(index_to_delete, inplace=True)

        # df.to_excel(path, index=False)

        # self.load_Data_Frame()
        # self.load_Data()
    

