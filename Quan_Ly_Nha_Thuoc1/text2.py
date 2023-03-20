import tkinter as tk
from tkinter import ttk

# Tạo một cửa sổ mới
root = tk.Tk()
root.geometry('300x200')

# Tạo một Treeview
tree = ttk.Treeview(root)
tree.pack()

# Thêm các cột cho Treeview
tree['columns'] = ('Name', 'Age', 'Gender')

# Đặt tên cho các cột
tree.heading('#0', text='ID')
tree.heading('Name', text='Name')
tree.heading('Age', text='Age')
tree.heading('Gender', text='Gender')

# Thêm dữ liệu cho Treeview
tree.insert('', 'end', text='001', values=('John', '25', 'Male'))
tree.insert('', 'end', text='002', values=('Mary', '30', 'Female'))
tree.insert('', 'end', text='003', values=('Tom', '20', 'Male'))
tree.insert('', 'end', text='004', values=('Lucy', '27', 'Female'))

# Tạo một Entry để hiển thị thông tin của hàng được chọn
entry = tk.Entry(root)
entry.pack()

# Định nghĩa hàm để in ra thông tin của hàng được chọn
def show_selected_row(event):
    item = tree.focus()
    values = tree.item(item, 'values')
    entry.delete(0, tk.END)
    entry.insert(0, values)

# Khi click vào một hàng trong Treeview, gọi hàm show_selected_row
tree.bind('<<TreeviewSelect>>', show_selected_row)

root.mainloop()