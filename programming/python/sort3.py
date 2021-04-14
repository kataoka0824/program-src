def perm(a,n,A):
    if n==0:
        print(a)
        return A
    else:
        for i in range(n-1):
            box=a[i+1]
            a[i+1]=a[i]
            a[i]=box
            A.append(a)
    return perm(a[0:n-1],len(a[0:n-1]),A)
import sys
A=[]
a = sys.argv[1:]
A.append(a)
# ソートを実行し、結果を表示する。
A1=perm(a,len(a),A)
print(A1)
