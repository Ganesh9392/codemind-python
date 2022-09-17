n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(len(l)-1,0,-1):
    if l[i]-l[i-1]>0:
        s+=l[i]-l[i-1]
print(s)