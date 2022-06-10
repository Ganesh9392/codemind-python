n=int(input())
l=list(map(int,input().split()))
ln=len(l)//2
l1=[]
for i in range(ln):
    l1.append(l[i])
    l1.append(l[-(i+1)])
if(len(l)%2==0):
    print(*l1)
else:
    l1.append(l[ln])
    l1.append(0)
    print(*l1)