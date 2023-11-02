from tkinter import *

def click(event):
    global var
    text = event.widget.cget("text")
    if(text) == "=":
        if var.get().isdigit():
            value = int(var.get())
        else:
            try:
                value = eval(var.get())
            except:
                var.set("Error")
                entry.update()
        var.set(value)
        entry.update()

    elif text == "C":
        var.set("")
        entry.update()
    else:
        var.set(var.get()+ text)
        entry.update()

basic = Tk()

basic.title("Calculator -- Made by M.Hassan")
basic.geometry("450x630")
basic.config(background="skyblue")
var = StringVar()
var.set("")

Label(basic, text="Calculator" , font= "14").pack()

entry = Entry(basic,textvariable=var, font = "lucida 40 bold" , borderwidth=10)
entry.pack(fill=X , pady=10, ipadx= 8 )

f = Frame(basic , bg="grey")

button =Button(f, text="/", padx=13 ,font="lucida 25 bold")
button.pack(padx=19,pady=8, side=LEFT)
button.bind("<Button-1>", click)

button =Button(f, text="*", padx=7 ,font="lucida 25 bold")
button.pack(padx=21, pady=8, side=LEFT)
button.bind("<Button-1>", click)

button =Button(f, text="=", padx=8 ,font="lucida 25 bold")
button.pack(padx=20, pady=8, side=LEFT)
button.bind("<Button-1>", click)

f.pack()

f = Frame(basic , bg="grey")

button =Button(f, text="C", padx=7 ,font="lucida 25 bold")
button.pack(padx=20,pady=8, side=LEFT)
button.bind("<Button-1>", click)

button =Button(f, text="+", padx=7 ,font="lucida 25 bold")
button.pack(padx=20, pady=8, side=LEFT)
button.bind("<Button-1>", click)

button =Button(f, text="-", padx=7 ,font="lucida 25 bold")
button.pack(padx=20, pady=8, side=LEFT)
button.bind("<Button-1>", click)

f.pack()

f = Frame(basic , bg="grey")

button =Button(f, text="0", padx=7 ,font="lucida 25 bold")
button.pack(padx=20,pady=8, side=LEFT)
button.bind("<Button-1>", click)

button =Button(f, text="1", padx=7 ,font="lucida 25 bold")
button.pack(padx=20, pady=8, side=LEFT)
button.bind("<Button-1>", click)

button =Button(f, text="2", padx=7 ,font="lucida 25 bold")
button.pack(padx=20, pady=8, side=LEFT)
button.bind("<Button-1>", click)

f.pack()

f = Frame(basic , bg="grey")

button =Button(f, text="3", padx=7 ,font="lucida 25 bold")
button.pack(padx=20, pady=8, side=LEFT)
button.bind("<Button-1>", click)

button =Button(f, text="4", padx=7 ,font="lucida 25 bold")
button.pack(padx=20, pady=8, side=LEFT)
button.bind("<Button-1>", click)

button =Button(f, text="5", padx=7 ,font="lucida 25 bold")
button.pack(padx=20, pady=8, side=LEFT)
button.bind("<Button-1>", click)

f.pack()

f = Frame(basic , bg="grey")

button =Button(f, text="6", padx=7 ,font="lucida 25 bold")
button.pack(padx=20, pady=8, side=LEFT)
button.bind("<Button-1>", click)

button =Button(f, text="7", padx=7 ,font="lucida 25 bold")
button.pack(padx=20, pady=8, side=LEFT)
button.bind("<Button-1>", click)

button =Button(f, text="8", padx=7 ,font="lucida 25 bold")
button.pack(padx=20, pady=8, side=LEFT)
button.bind("<Button-1>", click)

f.pack()


f = Frame(basic , bg="grey")

button =Button(f, text="7", padx=7 ,font="lucida 25 bold")
button.pack(padx=20, pady=8, side=LEFT)
button.bind("<Button-1>", click)

button =Button(f, text="8", padx=7 ,font="lucida 25 bold")
button.pack(padx=20, pady=8, side=LEFT)
button.bind("<Button-1>", click)

button =Button(f, text="9", padx=7 ,font="lucida 25 bold")
button.pack(padx=20, pady=8, side=LEFT)
button.bind("<Button-1>", click)

f.pack()


basic.mainloop()
