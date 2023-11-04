from tkinter import *
from tkinter.font import Font

def delete_btn():
    listb.delete(END,ANCHOR)

def insert_btn():
    listb.insert(END,my_entry.get())
    my_entry.delete(0,END)

def update_btn():
    select = listb.curselection()
    if select:
        index = int(select[0])
        text = my_entry.get()
        listb.delete(index)
        listb.insert(index , text)
        my_entry.delete(0,END)


root = Tk()
root.geometry("644x650")
root.title("To do list ---By M.Hassa")

root.config(bg="skyblue")
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


labelb = Label(root, text="Enter Here :", font="Calbria 18").pack(pady=10)
my_entry = Entry(root,font=my_font)
my_entry.pack(pady=10)

Btn_Frame = Frame(root)
Btn_Frame.pack(pady=10)

delbtn = Button(Btn_Frame , text="Delete Button" , command=delete_btn)
insertbtn = Button(Btn_Frame , text="Insert Button" , command=insert_btn)
updatebtn = Button(Btn_Frame , text="Update Button" , command=update_btn)

delbtn.grid(row=0 , column=0,padx=5)
insertbtn.grid(row=0 , column=1,padx=5)
updatebtn.grid(row=0 , column=2, padx=5)

root.mainloop()