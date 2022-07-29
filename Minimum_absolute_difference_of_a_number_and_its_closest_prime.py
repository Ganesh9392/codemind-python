n=int(input())
c=0
l1=0
l2=0
for i in range (1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print(0)
else:
    for i in range(n-1,1,-1):
        c=0
        for j in range(1,i):
            if i%j==0:
                c+=1
        if c==1:
            l1=i
            break
    for i in range(n+1,n+100,1):
        c=0
        for j in range(1,i):
            if i%j==0:
                c+=1
        if c==1:
            l2=i
            break
    d1=n-l1
    d2=l2-n
    print(min(d1,d2))