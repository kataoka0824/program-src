def insort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j+1]<a[j]:
                box=a[j+1]
                a[j+1]=a[j]
                a[j]=box
    return
import sys
a = []
for i in range(len(sys.argv)-1):
    v = int(sys.argv[i+1])
    a = a + [v]
# ソートを実行し、結果を表示する。
insort(a)
print(a)
