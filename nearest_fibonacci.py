n=int(input())
a=0
b=1
c=1
l1=[0,1]
l2=[]
l3=[]
for i in range(n):
    c=a+b
    a=b
    b=c
    l1.append(c)
if(n in l1):
    l1.remove(n)
for i in range(len(l1)):
    if(l1[i]>n):
        l3.append(l1[i])
    else:
        l2.append(l1[i])
l=len(l2)
if(n<l2[l-1]):
    r1=l2[1-1]-n
else:
    r1=n-l2[l-1]
r2=l3[0]-n

if(r2==r1):
    print(l2[l-1],l3[0])
elif(r2>r1):
    print(l2[l-1])
else:
    print(l3[0])