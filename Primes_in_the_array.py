num=int(input())
l=list(map(int,input().split()))
c=0
c1=0
for i in range(len(l)):
    c=0
    for j in range(1,l[i]):
        if(l[i]%j==0):
            c+=1
    if(c==1):
        c1+=1
print(c1)