import tkinter
import tkinter.messagebox
import tkinter.font as font
from tkinter.ttk import *
from turtle import bgcolor
frame = tkinter.Tk()
frame.title(" calculator ")

sample_text = tkinter.Entry(frame,width=10,font=('Arial 50'))
sample_text.place(x=600,y=100)

def button_text(text):
 sample_text.insert(0, text)


#helloworld
P1 = tkinter.Button(frame , text = ".", height = 1, width = 3, font= font.Font(size=30), bg= "black", activebackground= "white",fg="white")
M1 = tkinter.Button(frame , text = "+", height = 1, width = 3, font= font.Font(size=30), bg= "black", activebackground= "white",fg="white")
M2 = tkinter.Button(frame , text = "-", height = 1, width = 3, font= font.Font(size=30), bg= "black", activebackground= "white",fg="white")
M3 = tkinter.Button(frame , text = "x", height = 1, width = 3, font= font.Font(size=30), bg= "black", activebackground= "white",fg="white")
M4 = tkinter.Button(frame , text = "÷", height = 1, width = 3, font= font.Font(size=30), bg= "black", activebackground= "white",fg="white")
M5 = tkinter.Button(frame , text = "=", height = 1, width = 3, font= font.Font(size=30), bg= "black", activebackground= "white",fg="white")
B1 = tkinter.Button(frame , text = "1", command = button_text , height = 1, width = 3, font= font.Font(size=30), bg= "black", activebackground= "white",fg="white")
B2 = tkinter.Button(frame , text = "2", height = 1, width = 3, font= font.Font(size=30), bg= "black", activebackground= "white",fg="white")
B3 = tkinter.Button(frame , text = "3", height = 1, width = 3, font= font.Font(size=30), bg= "black", activebackground= "white",fg="white")
B4 = tkinter.Button(frame , text = "4", height = 1, width = 3, font= font.Font(size=30), bg= "black", activebackground= "white",fg="white")
B5 = tkinter.Button(frame , text = "5", height = 1, width = 3, font= font.Font(size=30), bg= "black", activebackground= "white",fg="white")
B6 = tkinter.Button(frame , text = "6", height = 1, width = 3, font= font.Font(size=30), bg= "black", activebackground= "white",fg="white")
B7 = tkinter.Button(frame , text = "7", height = 1, width = 3, font= font.Font(size=30), bg= "black", activebackground= "white",fg="white")
B8 = tkinter.Button(frame , text = "8", height = 1, width = 3, font= font.Font(size=30), bg= "black", activebackground= "white",fg="white")
B9 = tkinter.Button(frame , text = "9", height = 1, width = 3, font= font.Font(size=30), bg= "black", activebackground= "white",fg="white")
B0 = tkinter.Button(frame , text = "0", height = 1, width = 3, font= font.Font(size=30), bg= "black", activebackground= "white",fg="white")

B7.place(x=600,y=200)
B8.place(x=700,y=200)
B9.place(x=800,y=200)
B4.place(x=600,y=300)
B5.place(x=700,y=300)
B6.place(x=800,y=300)
B1.place(x=600,y=400)
B2.place(x=700,y=400)
B0.place(x=600,y=500)
B3.place(x=800,y=400)
M1.place(x=700,y=500)
M2.place(x=800,y=500)
M3.place(x=900,y=400)
M4.place(x=900,y=300)
M5.place(x=900,y=200)
P1.place(x=900,y=500)
#A1.pack()


frame.mainloop()