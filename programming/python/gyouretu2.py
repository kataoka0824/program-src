import sys
import tkinter as tk
import numpy as np
#強制終了
def end():
	sys.exit()
#行列の個数定義の判定
def jud_k():
	if e_s.get().isdecimal():
		global e_s_a
		e_s_a=e_s.get()
		root_s.quit()
		root_s.destroy()
	else:
		root_s.quit()
		sys.exit()
#行列のデータ化
def ok():
	global a
	a=[]
	a1=[]
	for j in range(3):
		for m in range(3):
			if e[j*3+m].get().isdecimal():
				a1.append(int(e[j*3+m].get()))
			else:
				a1.append(0)
		a.append(a1)
		a1=[]
	print(a)
	root.quit()
	root.destroy()
#行列の個数定義
root_s=tk.Tk()
root_s.title("行列の数")
root_s.geometry("300x100")
l_s=tk.Label(text="行列の数を入力")
l_s_1=tk.Label(text="k=")
e_s=tk.Entry(width=2)
b_s=tk.Button(text="ok",command=jud_k)
#ウィジェットの配置
l_s.grid(row=0,column=0)
l_s_1.grid(row=1,column=0)
e_s.grid(row=1,column=1)
b_s.grid(row=1,column=2)
root_s.mainloop()
#要素の当てはめ
mat=1
for i in range(int(e_s_a)):
	root=tk.Tk()
	root.title("行列")
	root.geometry("200x200")
	e=[]
	var=tk.StringVar()
	var.set(str(i+1)+"番目の行列")
	for j in range(9):
		e.append(tk.Entry(root,width=2))
	l=tk.Label(root,textvariable=var)
	b=tk.Button(root,text="ok",command=ok,width=2)
	b_1=tk.Button(root,text="やめる",command=end,width=2)


	#ウィジェットの配置
	l.grid(row=0,column=0,padx=3,pady=3)
	for j in range(3):
		for m in range(3):
			e[j*3+m].grid(row=j+1,column=m,padx=18,pady=5)
	b.grid(row=4,column=0,padx=3,pady=3)
	b_1.grid(row=4,column=2,padx=3,pady=3)
	root.mainloop()
	mat=np.dot(mat,a)
root1=tk.Tk()
root1.title("行列の積")
root1.geometry("200x200")
l_1_1=tk.Label(root1,text="行列の積")
l_1_1.grid(row=0,column=0,padx=3,pady=5)
var1=[]
l_1_2=[]
b_1_1=tk.Button(root1,text="ok",command=end)
for i in range(3):
	for j in range(3):
		var1.append(tk.StringVar())
		var1[i*3+j].set(str(mat[i][j]))
		l_1_2.append(tk.Label(root1,textvariable=var1[i*3+j]))
		l_1_2[i*3+j].grid(row=i+1,column=j,padx=18,pady=5)
b_1_1.grid(row=4,column=0,padx=3,pady=5)
root1.mainloop()
print(mat)
