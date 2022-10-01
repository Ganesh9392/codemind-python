num=int(input())
l=list(map(int,input().split()))
x=int(input())
l1=[]
for i in range(len(l)):
    if l[i]==x:
        l1.append(i)
if len(l1) != 0:
    print(l1[0],l1[-1])
else:
    print(-1,-1)