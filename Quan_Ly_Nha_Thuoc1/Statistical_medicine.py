import matplotlib.pyplot as plt
import pandas as pd
from tkinter import *

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Statistical():
    def __init__(self, root):
        self.root = root

        self.frame = Frame(root, width=900, height=700)
        self.frame.configure(bg='grey')

        # Đọc dữ liệu từ file Excel
        df = pd.read_excel('Sales_medicine.xlsx')

        # Tạo một đối tượng Figure và một đối tượng Axes của Matplotlib
        fig = Figure(figsize=(10, 16), dpi=100)
        ax = fig.add_subplot(111)

        # Tạo một biểu đồ cột sử dụng Matplotlib
        ax.bar(df['ngayMua'], df['so_luong'])

        # Đặt tiêu đề và các nhãn trục cho biểu đồ
        ax.set_title('Tổng kết thuốc')
        ax.set_xlabel('ngayMua')
        ax.set_ylabel('so_luong')

        # Tạo một đối tượng FigureCanvasTkAgg của Matplotlib để hiển thị biểu đồ trong frame
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

