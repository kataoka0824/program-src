import sys
import tkinter as tk
def click():
	e=textbox1.get()
	var.set(e)
	var1.set("")
root=tk.Tk()
root.title("tk-test")
root.geometry("600x400")
var=tk.StringVar()
var1=tk.StringVar()
var.set("text")
var1.set("text")
text1=tk.Label(textvariable=var)
text1.pack()
textbox1=tk.Entry(textvariable=var1,width=10)
textbox1.pack()
button1=tk.Button(text="ok",command=click)
button1.pack()
root.mainloop()