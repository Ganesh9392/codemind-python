n=int(input())
l=list(map(int,input().split()))
r=[]
for i in range(len(l)):
    p=1
    if l[i]>=1:
        t=i
        for j in range(len(l)):
            if j==t:
                continue
            else:
                p=p*l[j]
        print(p,end=" ")
    else:
        print(l[i],end=" ")