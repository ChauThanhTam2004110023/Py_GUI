from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import tkinter as tk
import pandas as pd



class Help():
    def __init__(self, username, root) -> None:
        self.root = root
        self.username=username


        self.df = pd.DataFrame(columns=['name', 'email', 'help_text'])
        
        self.frame = Frame(self.root, width=1000, height=700)
        self.frame.configure(bg='grey')


        lb_1 = Label(self.frame, text="Nhập họ tên", font="arail 10 bold", fg='blue')
        lb_1.place(x=50, y=30)
        self.entry_1 = Entry(self.frame, bd=3 ,width=40, font='arail 10')
        self.entry_1.place(x=250, y=30)

        lb_2 = Label(self.frame, text='Nhập email người gửi', font='arail 10 bold', fg='blue')
        lb_2.place(x=50, y=100)
        self.entry_2 = Entry(self.frame, bd=3 ,width=40, font='arail 10')
        self.entry_2.place(x=250, y=100)


        lb_5 =Label(self.frame, text="Nhập ý kiến cần trợ giúp", font="arail 10 bold", fg="blue")
        lb_5.place(x=50, y=200)
        self.entry_3 = Entry(self.frame ,width=100, font="arail 10")
        self.entry_3.place(x=250, y=200, height=20)

        self.butt = Button(self.frame, text="Submit", font="arail 10 bold", command=self.helpData)
        self.butt.place(x=250, y=300)

    def helpData(self):
        name = self.entry_1.get()
        email = self.entry_2.get()
        help_text = self.entry_3.get()
        
        # add data to dataframe
        self.df = self.df.append({'name': name, 'email': email, 'help_text': help_text}, ignore_index=True)
        
        # export dataframe to Excel file
        writer = pd.ExcelWriter('Help.xlsx', engine='xlsxwriter')
        self.df.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        
        # show success message
        messagebox.showinfo("Success", "Your request has been submitted.")
    