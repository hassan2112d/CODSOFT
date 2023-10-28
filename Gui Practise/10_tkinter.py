from tkinter import *

a = Tk()

canvas_width = 900

canvas_height = 500

a.geometry(f"{canvas_width}x{canvas_height}")
a.title("Intership")

canvas_widget = Canvas(a, width=canvas_width, height=canvas_height)
canvas_widget.pack()

canvas_widget.create_line(0,0,800,450 , fill="red")
canvas_widget.create_line(0,450,800,0 , fill="red")

canvas_widget.create_rectangle(244,20,400,250 , fill="blue")
canvas_widget.create_text(350,150, text="python")

canvas_widget.create_oval(250,60,120,250, fill="red")

a.mainloop()