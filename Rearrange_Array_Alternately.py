num=int(input())
for i in range(num):
    n=int(input())
    l=list(map(int,input().split()))
    x=len(l)//2
    t=l[x]
    l1=[]
    for j in range(x):
        l1.append(max(l))
        l.remove(max(l))
        l1.append(min(l))
        l.remove(min(l))
    if len(l)%2==0:
        print(*l1)
    else:
        l1.append(t)
        print(*l1)
    