from tkinter import *

a = Tk()

a.title("Newspaper")

a.geometry("1200x600")

e= "Spder man is missing after his movie homecoming"

h = "Nature is a blessing and beautiful thing in the world."

c = PhotoImage(file="Gui Practise/spider.png", width=300 ,height=300)

g = PhotoImage(file="Gui Practise/palestine.png", width=300 , height=300)

b= Label(text="Welcome to newspaper")

d = Label(image=c)

j= Label(image=g)

f = Label(text=e)

i = Label(text=h)

b.pack()
d.pack()
f.pack( )
j.pack(side="bottom")
i.pack()


a.mainloop()