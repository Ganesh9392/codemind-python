n=int(input())
k=list(map(int,input().split()))
a,b=map(int,input().split())
p=max(a,b)
s=min(a,b)
c=0
for i in range(len(k)):
    if k[i]>p or k[i]<s:
        c+=1
        print(k[i],end=" ")
if c==0:
    print("-1")
    