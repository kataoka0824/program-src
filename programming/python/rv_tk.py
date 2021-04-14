import tkinter as tk
def ok(e1):
    print(e1.get())
root=tk.Tk()
root.title("アプリケーション")
root.geometry("300x100")
l1=tk.Label(text="写真のデータ：")
l1.pack(side="left")
e1=tk.Entry()
e1.pack(side="left")
b1=tk.Button(text="ok",command=ok(e1))
b1.pack(side="left")
root.mainloop()
