n=int(input())
l=[0,1]
a=0
b=1
c=0
for i in range(n-2):
    c=a+b
    l.append(c)
    a=b
    b=c
print(*l)