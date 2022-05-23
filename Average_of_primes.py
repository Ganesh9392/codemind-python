num=int(input())
l=list(map(int,input().split()))
l1=[]
c=0
for i in range(len(l)):
    c=0
    for j in range(1,l[i]):
        if(l[i]%j==0):
            c=c+1
    if(c==1):
        l1.append(l[i])
r=sum(l1)/len(l1)
print("{0:.2f}".format(r))