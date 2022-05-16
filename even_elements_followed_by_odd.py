num=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)-1):
    if(l[i]%2==0):
        l1.append(l[i])
if(l[num-1]%2==0):
    l1.append(l[num-1])
for j in range(len(l)-1):
    if(l[j]%2==1):
        l1.append(l[j])
if(l[num-1]%2==1):
    l1.append(l[num-1])
for k in range(len(l1)):
    print(l1[k],end=" ")