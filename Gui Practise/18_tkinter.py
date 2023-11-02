from tkinter import *

a = Tk()

a.title("Scroll Bar")

a.geometry("800x800")

scroll = Scrollbar(a)
scroll.pack( side=RIGHT , fill=Y )

label = Text(a, yscrollcommand = scroll.set())
label.pack(fill=BOTH)

label.config(command=scroll.yview)



a.mainloop()