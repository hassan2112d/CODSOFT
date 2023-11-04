from tkinter import *
from random import randint


def generate_pass():
    pass_entry.delete(0, END)

    my_lenght = int(my_entry.get())
    
    my_password = ''

    for x in range(my_lenght):
        my_password += chr(randint(32, 126))

    pass_entry.insert(0 , my_password)

root = Tk()

root.title("Password Generator --- by M.Hassan")
root.geometry("600x500")

root.config(bg="grey")
my_password = chr(randint(33,120))

header = Label(text="Password Generator").pack(pady=10)

head = LabelFrame(root ,  text="Enter the Length to generate a Password :")
head.pack(pady=50)

my_entry = Entry(head, font="Helvetica 24" )
my_entry.pack(pady=5)

head1 = LabelFrame(root , text="Generated Password :")
head1.pack()
pass_entry = Entry(head1, font="Calbria 24")
pass_entry.pack(pady=5)

btn = Button(root,text="Generate Password",bg="yellow", command=generate_pass)
btn.pack(pady=5)
root.mainloop()