n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
r=[]
for i in range(len(l)):
    if i%2==0:
        l1.append(l[i])
    else:
        l2.append(l[i])
for i in range(len(l1)):
    for j in range(l1[i]):
        r.append(l2[i])
print(*r)