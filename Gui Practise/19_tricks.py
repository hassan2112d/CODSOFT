from tkinter import *

a = Tk()
a.geometry("800x900")
a.title("Welcome to Codeix -- coding paltform")
a.wm_iconbitmap("Gui Practise/palestine.png")
a.configure(background="grey")

Button(text="close" , command=a.destroy).pack()

a.mainloop()