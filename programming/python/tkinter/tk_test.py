import tkinter as tk
import tkinter.ttk as ttk
import sys
import csv
import numpy as np
filename="data.csv"
#終了コマンド
def close():
    sys.exit()
#結果表示
def show():
    root2=tk.Toplevel()
    root2.title("結果")
    root2.geometry("300x100")
    text2_1=tk.Label(root2,text=entry1.get())
    text2_1.grid(row=0,column=0)
#データ追加
def add_data():
    word=entry3.get()
    mean=entry3_1.get("1.0","end -1c")
    print(word,mean)
    with open(filename,"a") as f:
        writer=csv.writer(f)
        writer.writerow([word,mean])
#データ追加画面
def add_data_win():
    global entry3,entry3_1
    root3=tk.Toplevel()
    root3.title("追加")
    root3.geometry("800x600")
    text3=tk.Label(root3,text="単語:")
    text3.grid(row=0,column=0)
    text3_1=tk.Label(root3,text="意味:")
    text3_1.grid(row=1,column=0)
    entry3=tk.Entry(root3,width=65)
    entry3.grid(row=0,column=1)
    button3=tk.Button(root3,text="追加",command=add_data)
    button3.grid(row=0,column=2)
    entry3_1=tk.Text(root3)
    entry3_1.grid(row=1,column=1)
#データ削除
def del_data():
    print(combo.get())
    for i in range(len(data)):
        if data[i][0]==combo.get():
            print(i)
            data.pop(i)
            break;
    with open(filename,"w") as f:
        writer=csv.writer(f)
        writer.writerows(data)
#データ削除画面
def del_data_win():
    global data,combo
    root4=tk.Toplevel()
    root4.title("削除")
    root4.geometry("300x100")
    text4=tk.Label(root4,text="単語:")
    text4.grid(row=0,column=0)
    with open(filename,"r") as f:
        reader=csv.reader(f)
        data=[row for row in reader]
    data_t=np.array(data).T.tolist()
    combo=ttk.Combobox(root4,state="readonly")
    combo["values"]=data_t[0]
    combo.current(0)
    combo.grid(row=0,column=1)
    button4=tk.Button(root4,text="削除",command=del_data)
    button4.grid(row=0,column=2)
#メイン画面
root=tk.Tk()
root.title("test")
root.geometry("300x100")
text1=tk.Label(text="単語:")
text1.grid(row=0,column=0)
entry1=tk.Entry()
entry1.grid(row=0,column=1)
button1=tk.Button(text="検索",command=show)
button1.grid(row=0,column=2)
button1_1=tk.Button(text="閉じる",command=close)
button1_1.grid(row=1,column=1)
#メニュー
menubar=tk.Menu(root)
root.config(menu=menubar)
menu1=tk.Menu()
menubar.add_cascade(label="メニュー",menu=menu1)
menu1.add_command(label="追加",command=add_data_win)
menu1.add_command(label="削除",command=del_data_win)

root.mainloop()
