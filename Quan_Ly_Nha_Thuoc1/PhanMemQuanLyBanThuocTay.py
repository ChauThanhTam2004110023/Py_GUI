import tkinter as tk
from tkinter import *
from tkinter import ttk
import UIUpdate
import UIAccount
import UILogin
import Supplier
import Sales_medicine
import Help
import Type_of_medicine
import Statistical_medicine
import Statistical_type_of_medicine
from tkinter.ttk import Progressbar







def startUp():

    global menuBar, loginGUI,username,currentFrame,accountFrame,accountUpdateUI,accountsupplierUI,accounttype_of_medicine,account_help,account_sales,statistical_account,statistical_type_of_medicine
    menuBar=createMenu(root)


    # login

    loginGUI=UILogin.UILogin(root,afterLoginSetup)
    username=loginGUI.username


    # main

    accountUI=UIAccount.UIAccount(username,root)
    accountFrame=accountUI.frame 

    updateUI = UIUpdate.UIUpdate(username, root)
    accountUpdateUI = updateUI.frame

    supplierUI = Supplier.Supplier(username, root)
    accountsupplierUI = supplierUI.frame

    type_of_medicine = Type_of_medicine.Type_of_medicine(username, root)
    accounttype_of_medicine = type_of_medicine.frame

    help = Help.Help(username, root)
    account_help = help.frame

    sales = Sales_medicine.Sales_medicine(username, root)
    account_sales = sales.frame

    statistical_ = Statistical_medicine.Statistical(root)
    statistical_account = statistical_.frame

    statistical__ = Statistical_type_of_medicine.Statistical(root)
    statistical_type_of_medicine = statistical__.frame






def loading(root):
    frame = Frame(root)
    frame.pack()
    global images

    images = PhotoImage(file='img/pharmacy.png')
    frame.config(width=500,height=500)
    # win.overrideredirect(True)
    frame.config(background="#0F2544")
    welcome_lable = Label(frame,text="PHẦN MỀM QUẢN LÝ BÁN THUỐC TÂY", bg="#0F2544",
                        fg="#FFFFFF", font=("Trebuchet Ms", 15, "bold"))
    welcome_lable.place(x=70, y=25)
    bg_label = Label(frame, image=images,  bg="#0F2544")
    bg_label.place(x=130, y=65)
    progress_label = Label(frame, text="Loading...",  bg="#0F2544",
                        fg="#FFFFFF", font=("Trebuchet Ms", 15, "bold"))
    progress_label.place(x=190, y=330)

    progress = ttk.Style()
    progress.theme_use('clam')
    progress.configure("red.Horizontal.TProgressbar", background="white")
    progress = Progressbar(frame, orient=HORIZONTAL, length=400,
                        mode="determinate", style="red.Horizontal.TProgressbar")
    progress.place(x=60, y=370)

    def top():
        frame.destroy()
        startUp()

    i = 0

    def load():
        nonlocal i
        if i <= 10:
            txt = 'Loading ... ' + (str(10*i) + '%')
            progress_label.config(text=txt)
            progress_label.after(600, load)
            progress['value'] = 10*i
            i += 1
        else:
            top()

    load()






def createMenu(win):
    menuBar = Menu(win)

    fileMenu = Menu(menuBar, tearoff=0)

    fileMenu.add_command(label="Đăng xuất",command=logOut)
    fileMenu.add_separator()
    fileMenu.add_command(label="Thoát", command= win.quit)
    menuBar.add_cascade(label="Hệ thống", menu = fileMenu)

    #danh muc
    editMenu = Menu(menuBar, tearoff= 0 )
    editMenu.add_command(label="Quản lý thuốc", command=  lambda: changeFrameClick(accountUpdateUI)  )
    editMenu.add_command(label="Loại thuốc", command=  lambda: changeFrameClick(accounttype_of_medicine)  )
    editMenu.add_command(label="Nhà cung cấp", command=  lambda: changeFrameClick(accountsupplierUI)  )
    menuBar.add_cascade(label="Danh mục", menu=editMenu)
    #search
    #bao cao thong ke


    fileMenu_1 = Menu(menuBar, tearoff=0)
    fileMenu_1.add_command(label="Loại thuốc", command= lambda: changeFrameClick(statistical_type_of_medicine) )

    fileMenu_1.add_command(label="thống kê người mua", command=  lambda: changeFrameClick(statistical_account)  )
    fileMenu_1.add_command(label="Mua thuốc", command=  lambda: changeFrameClick(account_sales)  )
    menuBar.add_cascade(label="Báo cáo thống kê", menu=fileMenu_1)

    # help
    menuBar.add_cascade(label="Trợ giúp", command=  lambda: changeFrameClick(account_help)  )

    return menuBar



#menu button

def changeFrameClick( frameToChange):
    global currentFrame
    if currentFrame is not None:
        currentFrame.pack_forget()
    currentFrame=frameToChange
    currentFrame.pack()




def afterLoginSetup():
    global menuBar, root, username
    menuBar =  createMenu(root)
    root.config(menu=menuBar)
    username=loginGUI.username
    if username == "admin":
        menuBar.add_cascade(label="Quản lý tài khoản",command=  lambda: changeFrameClick(accountFrame)  )



def logOut():
    global menuBar, root,loginGUI
    root.config(menu=Menu(root)) 
    if currentFrame is not None:
        currentFrame.pack_forget()
    loginGUI.mainFrame.pack()


    

    

# 1111111111111111111111111111111111111111111111111111111111111

root = tk.Tk()
root.title(string='PHẦN MỀM QUẢN LÝ BÁN THUỐC TÂY')




menuBar=None


# login

loginGUI=None
username=None


# main
currentFrame=None


accountFrame=None


accountUpdateUI = None


accountsupplierUI =None

accounttype_of_medicine = None

account_help =None

account_sales =None

statistical_account = None

statistical_type_of_medicine =None


loading(root)
root.mainloop()
