import tkinter as tk
import Sales_medicine

class MyFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # Tạo nút thoát khung
        exit_button = tk.Button(self, text="Thoát", command=self.quit)
        exit_button.pack(side="bottom")

    def quit(self):
        # Đóng khung
        self.destroy()


root = tk.Tk()
my_frame = Sales_medicine()
my_frame.__init__
my_frame.pack()
root.mainloop()
