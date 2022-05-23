num=int(input())
l=list(map(int,input().split()))
l1=[]
c=0
c1=0
n=int(input())
for i in range(len(l)):
    if(n>=l[i]):
        l1.append(l[i])
for j in range(len(l1)):
    c=0
    for k in range(1,l1[j]):
        if(l1[j]%k==0):
            c+=1
    if(c==1):
        c1=c1+1
print(c1)
            