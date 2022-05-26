n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
    t=l[i]
    while t:
        d=t%10
        t=t//10
        l1.append(d)
print(sum(l1))
        
        