n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
    if(l[i]%2==1):
        if l[i] not in l1:
            l1.append(l[i])
print(len(l1))