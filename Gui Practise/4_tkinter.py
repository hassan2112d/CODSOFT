from tkinter import *

a = Tk()

a.geometry("1200x800")
a.title("GUI Applications")

#labels = 
#Background color
#text
#Foreground
#Padding x and padding Y
#Font
#anchor 
#Fill = X
#Fill = Y

b = Label(text="Hello World ", bg="red", fg="white", padx=20 , pady= 60 , font=("calibri",22,UNDERLINE),borderwidth=40 , relief=SUNKEN )

b.pack(side="top", fill=X )


a.mainloop()