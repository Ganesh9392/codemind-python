n=int(input())
l=[]
l1=[]
for i in range(1,n+1):
    if(n%i==0):
        l.append(i)
for i in range(len(l)):
    c=0
    for j in range(1,l[i]+1):
        if(l[i]%j==0):
            c+=1
    if(c==2):
        pass
    else:
        l1.append(l[i])
print(len(l1))