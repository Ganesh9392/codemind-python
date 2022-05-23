num=int(input())
l=list(map(int,input().split()))
n=int(input())
s=0
for i in range(len(l)):
    if(l[i]<=n):
        s=s+l[i]
print(s)