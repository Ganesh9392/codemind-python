n=int(input())
a=0
b=1
l=[0,1]
l1=[]
l2=[]
for i in range(1,1+n):
    c=a+b
    a=b
    b=c
    l.append(c)
for i in range(len(l)):
    if l[i]<n:
        l1.append(l[i])
    else:
        l2.append(l[i])
if n in l:
    l.remove(n)
x=max(l1)
y=min(l2)
d1=n-max(l1)
d2=min(l2)-(n)
if(d1==d2):
    print(x,y)
elif(d1<d2):
    print(x)
else:
    print(y)

    