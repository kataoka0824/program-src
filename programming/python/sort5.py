import sys
import copy
def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]
A=[]
i=[]
a = sys.argv[1:]
A2=[]
A3=[]
for i in range(len(a)):
    A2.append(0)
for i1 in range(len(a)):
    A2[0]=a[i1]
    for i2 in range(len(a)):
        A2[1]=a[i2]
        for i3 in range(len(a)):
            A2[2]=a[i3]
            for i4 in range(len(a)):
                A2[3]=a[i4]
                A=copy.deepcopy(A)
                A.append(A2)
for i in range(len(a)**len(a)):
    if len(dict.fromkeys(A[i])) == len(a):
        A3.append(A[i])
print(A3)
print(len(A3))

# ソートを実行し、結果を表示する。

