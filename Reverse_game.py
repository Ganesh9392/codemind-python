n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
    t=l[i]
    r=0
    while t:
        d=t%10
        r=r*10+d
        t=t//10
    l1.append(r)
for j in range(len(l1)):
    print(l1[j],end=" ")
        
        