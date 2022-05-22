num=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
l1=[]
s=min(a,b)
d=max(a,b)
c=0
for i in range(len(l)):
    if(l[i]>=s and l[i]<=d):
        l1.append(l[i])
        c=c+1
if(c==0):
    print(-1)
else:
    print(min(l1))