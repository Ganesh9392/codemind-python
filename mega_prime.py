n=int(input())
t=n
c=0
c1=0
l=[]
for i in range(1,n):
    if(n%i==0):
        c+=1
if(c==1):
    while n:
        d=n%10
        n=n//10
        c1=0
        for j in range(1,d+1):
            if(d%j==0):
                c1+=1
        if(c1==2):
            l.append(0)
        else:
            l.append(1)
    if max(l)==0:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
