import matplotlib.pyplot as plt
import csv
import numpy as np
fig = plt.figure()
ax = plt.axes()
ax.set_ylim([0,-20])
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
ax.scatter(l_x,l_y,c="gray",s=3)
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
ax.scatter(l_x,l_y,c="blue",s=10)
ax.set_aspect('equal')
#
for i in range(1):
    sx1=[]
    sy1=[]
    bx=[]
    by=[]
    for j in range(len(l_x)-1):
        if i!=j:
            m=-(l_x[j]-l_x[i])/(l_y[j]-l_y[i])
            x_1=(l_x[i]+l_x[j])/2
            y_1=(l_y[i]+l_y[j])/2
            b=y_1-x_1*m
            sx=np.arange(0,20,0.1)
            sy=m*sx+b
            sx1.append(sx)
            sy1.append(sy)
            #ax.plot(sx,sy)
    for j in range(len(l_x)-2):
        ax.plot(sx1[j],sy1[j])
        for k in range(200):
            if j>0:
                if abs(sy1[j][k]-sy1[j-1][k])<0.01:
                    print(sx1[j][k],sy1[j][k])
                    bx.append(sx1[j][k])
                    by.append(sy1[j][k])
                    
        #print(sx1[j],sy1[j])
        #ax.plot(sx1[j],sy1[j],color="black",markersize=10)
        ax.scatter(bx,by,c="black",s=10)
#地図表示
plt.show()
#svg変換
fig.savefig("voronoi1.svg",dpi=300)
