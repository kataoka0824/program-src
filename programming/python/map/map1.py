import matplotlib.pyplot as plt
import csv
fig = plt.figure()
ax = plt.axes()
#deaths
l_x=[]
l_y=[]
#csv読み込み
with open("Snow.deaths.csv") as f:
    reader=csv.reader(f)
    l=[row for row in reader]
#float変換
for i in range(1,len(l)):
    l_x.append(float(l[i][2]))
    l_y.append(-float(l[i][3]))
ax.scatter(l_x,l_y,c="red",s=5)
#pumps
l_x=[]
l_y=[]
label=[]
#csv読み込み
with open("Snow.pumps.csv") as f:
    reader=csv.reader(f)
    l1=[row for row in reader]
#float変換
for i in range(1,len(l1)):
    label.append(l1[i][2])
    l_x.append(float(l1[i][3]))
    l_y.append(-float(l1[i][4]))
for i in range(len(l1)-1):
    ax.text(l_x[i],l_y[i],label[i],size=7,color="black",horizontalalignment="center")
ax.scatter(l_x,l_y,c="blue",s=10)
#streets
x1=[]
y1=[]
n=[]
#csv読み込み
with open("Snow.streets.csv") as f:
    reader=csv.reader(f)
    l2=[row for row in reader]
#float変換
for i in range(1,len(l2)):
    x1.append(float(l2[i][3]))
    y1.append(-float(l2[i][4]))
    n.append(int(l2[i][2]))
    num=int(l2[-1][1])
space=0
sx=[]
sy=[]
#折れ線の作成
for i in range(num):
    for j in range(n[space]):
        sx.append(x1[space])
        sy.append(y1[space])
        space+=1
    plt.plot(sx,sy,color="gray")
    sx=[]
    sy=[]
ax.set_aspect('equal')
#地図表示
plt.show()
#svg変換
fig.savefig("map.svg",dpi=300)
