a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
for i in range(len(l1)):
    if(l1[i] not in l2):
        if(l1[i] not in l3):
            l3.append(l1[i])
for j in range(len(l2)):
    if(l2[j] not in l1):
        if(l2[j] not in l3):
            l3.append(l2[j])
print(*l3)