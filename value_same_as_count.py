n=int(input())
l=list(map(int,input().split()))
c=0
l1=[]
for i in range(len(l)):
    if(l[i]==l.count(l[i])):
        if(l[i] not in l1):
            l1.append(l[i])
            c+=1
print(c)