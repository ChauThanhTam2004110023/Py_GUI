from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import tkinter as tk
import pandas as pd


class UILogin():
    def __init__(self,root,command1) -> None:
        self.username=None
        self.mainFrame=Frame(root)
        main=self.mainFrame
        main.pack()

        def on_enter(e):
            username.delete(0,END)
    
        def on_leave(e):
            name = username.get()
            if name == '':
                username.insert(0,"Username")

        def on_enter_pass(e):
            password.delete(0, END)

        def on_leave_pass(e):
            passw = password.get()
            if passw == '':
                password.insert(0, "Password", show="*")

        def login():
            u=str(username.get())
            p=int(password.get())
            
            acc = self.search(["Username", "Password"], [u, p])
            if acc.empty == True:
                messagebox.showwarning(
                    "warning", message="username or password invalid")
            else:
                t = str(acc.iloc[0, 0])
                # messagebox.showinfo(message=t)
                self.mainFrame.pack_forget()
                self.username = t
                command1()
                
        
        img = PhotoImage(file="img/login.png")
        self.__image=img 
        Label(main, image=img , bg= "White" ).pack(side="left")
        frame = Frame(main, width=350, height=350, bg="white")
        frame.pack()
        heading = Label(frame, text="Sign in" , fg="#57a1f8" , bg="White", font=('Microsoft YaHei UI Light',23, "bold"))
        heading.place(x=100, y=5)
        username = Entry(frame, width=25, fg="black", border=0, bg="White", font=('Microsoft YaHei UI Light', 11))
        username.place(x=30, y=80)
        username.insert(0, "Username")
        username.bind('<FocusIn>',on_enter)
        username.bind('<FocusOut>',on_leave)
        Frame(frame, width=295, height=2, bg="black").place(x=25,y=107)
        password = Entry(frame, width=25, fg="black", border=0,bg="White", font=('Microsoft YaHei UI Light', 11))
        password.place(x=30, y=150)
        password.insert(0, "Password")
        password.bind('<FocusIn>', on_enter_pass)
        password.bind('<FocusOut>', on_leave_pass)
        Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)
        Button(frame, width=39 , pady= 7 , text="Sign in" , bg="#57a1f8" , fg="White" , border=0,command=login ).place(x=35, y= 204)
        label = Label(frame, text="Don't have an account? ", fg="black",bg="white", font=('Microsoft YaHei UI Light', 9))
        label.place(x=75,y=270)
        

    def search(self,conditionList, valueList):
        
        data = pd.ExcelFile('account.xlsx')
        df = pd.read_excel(data)
        df.drop(df.filter(regex="Unnamed"), axis=1, inplace=True)
        l = list(range(len(conditionList)))
        
        for i in l:
            df = df[df[str(conditionList[i])] == valueList[i]]
        return df