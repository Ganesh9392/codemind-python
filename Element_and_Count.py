num=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
    if(l[i] in l1):
        continue
    else:
        l1.append(l[i])
for j in range(len(l1)):
    print(l1[j],l.count(l1[j]),end=" ")