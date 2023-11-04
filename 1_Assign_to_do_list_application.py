from tkinter import *
from tkinter.font import Font

root = Tk()
root.geometry("644x650")
root.title("To do list ---By M.Hassa")

my_font = Font(
    family="Helvetica",  # Helvetica font for the text
    weight= "bold",
    size= 20
    

)

frm = Frame(root)
frm.pack(pady=5)

listb = Listbox(
    font=my_font,
    width=25,
    height=5,
    bg="SystemButtonFace",
    bd=0,
    fg = "#464646",
    borderwidth=20

)
listb.pack()

Stuff = ["Hello_World","helloooo","hassannn","Avina","Huda","Maya"]

for i in Stuff:
    listb.insert(END,i)

my_scroll = Scrollbar(frm)

my_scroll.pack(side="right",fill="both")
listb.config(yscrollcommand=my_scroll.set)

my_scroll.config(command=.yview)


root.mainloop()