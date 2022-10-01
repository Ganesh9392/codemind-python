def fun(t,x):
    c=0
    for i in range(len(x)):
        if t>x[i]:
            c+=1
    return c
n=int(input())
l=list(map(int,input().split()))
r=[]
for i in range(len(l)):
    r.append(fun(l[i],l))
print(*r)