num=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
s=min(a,b)
d=max(a,b)
l1=[]
for i in range(len(l)):
    if(l[i]<s or l[i]>d):
        c=c+1
        l1.append(l[i])
if(c==0):
    print(-1)
else:
    print(max(l1))