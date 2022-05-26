n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    t=l[i]
    r=0
    while t:
        d=t%10
        r=r*10+d
        t=t//10
    if(r==l[i]):
        c+=1
print(c)
        
        