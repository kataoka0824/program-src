a=1
jud=0
x=int(input("x="))
a=a%x
r=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
i=0
while a!=0:
    a=a*10
    d=a//x
    a=a%x
    print(f"digit={d},remainder={a}")
    r[i]=a
    i=i+1
    if i+1 != len(set(r)) or a==0:
        jud=1
        break;
print("r=",r)
if jud==1:
    print("junkan")
