def perm(a_b,a,n,A):
    if n==0:
        return A
    b1=a[:]
    box=b1[1]
    b1[1]=b1[0]
    b1[0]=box
    A.append(a_b+b1)
    b2=b1[:]
    box=b2[2]
    b2[2]=b2[1]
    b2[1]=box
    A.append(a_b+b2)
    return perm(a_b,b2,n-1,A)
import sys
A=[]
a = sys.argv[1:]
n=len(a)-1
s_a=a[n-2:]
b_a=a[0:n-2]
b_a_2=a[0:n-2]
for i in range(3):
    A=perm(b_a_2,s_a,len(s_a),A)
    box=a[n-3]
    a[n-3]=a[n-i]
    a[n-i]=box
    s_a=a[n-2:]
    b_a_2=a[0:n-2]
# ソートを実行し、結果を表示する。
print(A)
