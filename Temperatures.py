def fun(n,l):
    c=0
    for i in l:
        if i>n:
            return c
        else:
            c+=1
    return 0
n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    t=l[i:]
    print(fun(l[i],t),end=" ")
