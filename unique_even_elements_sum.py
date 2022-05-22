num=int(input())
l=list(map(int,input().split()))
m=set(l)
s=0
for i in m:
    if(i%2==0):
        s=s+i
print(s)