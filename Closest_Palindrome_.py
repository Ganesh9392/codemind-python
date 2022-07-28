n=int(input())
l=[]
l1=[]
for i in range(n-1,1,-1):
    t=i
    te=i
    r=0
    while t>0:
        d=t%10
        r=r*10+d
        t=t//10
    if(r==te):
        l.append(r)
l.sort()
for i in range(n,n+1000,+1):
    t=i
    te=i
    r=0
    while t>0:
        d=t%10
        r=r*10+d
        t=t//10
    if(r==te):
        l1.append(r)
l1.sort()
if(n in l1):
    l1.remove(n)
ln=len(l)
r1=l[ln-1]
r2=l1[0]
d1=n-r1
d2=r2-n
if(d1==d2):
    print(r1,r2)
elif(d1<d2):
    print(r1)
else:
    print(r2)