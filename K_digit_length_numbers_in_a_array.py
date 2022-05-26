a,b=map(int,input().split())
l=list(map(str,input().split()))
l1=[]
for i in range(len(l)):
    if(len(l[i])==b):
        l1.append(l[i])
    elif("+" in l[i] or "-"in l[i]):
        if(len(l[i])-1==b):
            l1.append(l[i])
print(len(l1))