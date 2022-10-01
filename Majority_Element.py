n=int(input())
l=list(map(int,input().split()))
mc=0
for i in range(len(l)):
    if l.count(l[i])>mc:
        mc=l.count(l[i])
        t=l[i]
print(t)