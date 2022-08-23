n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
l3=[]
for i in range(len(l)):
    if(i%2==1):
        l1.append(l[i])
    else:
        l2.append(l[i])
for i in range(len(l1)):
    for j in range(l1[i]):
        l3.append(l2[i])
print(*l3)