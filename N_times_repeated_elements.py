num=int(input())
l=list(map(int,input().split()))
n=int(input())
c=0
l1=[]
l2=[]
for i in range(len(l)):
    if(l.count(l[i])==n):
        c=c+1
        l1.append(l[i])
if(c==0):
    print(-1)
else:
    m=set(l1)
    l2=list(m)
    for j in range(len(l2)):
        print(l2[j],end=" ")