num=int(input())
l=list(map(int,input().split()))
l1=[]
c=0
for i in range(len(l)):
    if(l.count(l[i])==l[i]):
        l1.append(l[i])
        c=c+1
if(c==0):
    print(-1)
else:
    print(min(l1),max(l1))