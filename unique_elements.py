n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
    if(l[i] not in l1):
        l1.append(l[i])
for j in range(len(l1)):
    print(l1[j],end=" ")