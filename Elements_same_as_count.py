n=int(input())
l=list(map(int,input().split()))
l1=[]
c=0
for i in range(len(l)):
    if(l[i]==l.count(l[i])):
        if(l[i] not in l1):
            l1.append(l[i])
            c+=1
if(c==0):
    print(-1)
else:
    print(*l1)