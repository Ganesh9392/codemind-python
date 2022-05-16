num=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
r1=int(a)
r2=int(b)
big=max(r1,r2)
small=min(r1,r2)
c=0
for i in range(len(l)):
    if(l[i]<small or l[i]>big):
        c+=1
        print(l[i],end=" ")
if(c==0):
    print(-1)
    