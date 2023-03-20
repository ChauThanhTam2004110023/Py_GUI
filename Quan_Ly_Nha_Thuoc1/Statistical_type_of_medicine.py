import matplotlib.pyplot as plt
import pandas as pd
from tkinter import *

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Statistical():
    def __init__(self, root) -> None:
        self.root = root

        self.frame = Frame(root, width=900, height=700)
        self.frame.configure(bg='grey')

        df = pd.read_excel('Type_of_medicine.xlsx')

        fig = Figure(figsize=(10, 16), dpi=100)
        ax = fig.add_subplot(111)

        ax.bar(df['Tên loại thuốc'], df['Số lượng'])

        ax.set_title('Tổng kết các loại thuốc')
        ax.set_xlabel('Tên loại thuộc')
        ax.set_ylabel('Số lượng')

        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().pack()