import sys
def merge(a,n):
    k=[]
    m=a[:]
    k.append([m[0],m[1]])
    if m[0]>m[1]:
        k[0]=[m[1],m[0]]
    for i in range(n-2):
        k.append(mergesort(k[i],m[i+2],i+2))
    return k
def mergesort(k,A,n):
    m=k[:]
    for i in range(n):
        if A<m[i]:
            m.insert(i,A)
            break;
    if A>m[n-1]:
        m.append(A)
    return m
a = []
for i in range(len(sys.argv)-1):
    v = int(sys.argv[i+1])
    a = a + [v]
k=merge(a,len(a))
print(k[len(a)-2])
