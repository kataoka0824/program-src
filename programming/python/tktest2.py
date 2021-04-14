import sys
import tkinter as tk

root=tk.Tk()
root.title("tk-test")
root.geometry("600x400")
e=[]
for i in range(9):
	e.append(tk.Entry(width=2))
for i in range(3):
	for j in range(3):
		e[i*3+j].grid(row=i,column=j,padx=2,pady=2)
root.mainloop()

