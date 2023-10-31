from tkinter import *

def harry(event):
    print(f"the x axises is {event.x} and y is {event.y}")
a = Tk()

a.title("Events")
a.geometry("600x500")

b = Button(a , text="Click ON mE" , bg="RED")

b.pack()

b.bind('<Button-1>', harry)
b.bind('<Double-1>' , quit)


a.mainloop()