def fun(l,n):
    p=n
    l1=["0"]*len(l)
    for i in l:
        if p>len(l)-1:
            p=p-len(l)
        l1[p]=i
        p+=1
    return l1
num=int(input())
for i in range(num):
    n,p=map(int,input().split())
    l=list(map(int,input().split()))
    print(*fun(l,p))
    
