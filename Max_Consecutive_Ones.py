n=int(input())
l=list(map(int,input().split()))
mc=0
c=0
for i in range(len(l)):
    if l[i]==1:
        c+=1
        if c>mc:
            mc=c
    else:
        c=0
print(mc)