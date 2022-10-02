n=int(input())
l=[]
t=n
for i in range(n+1):
    l.append(2**i)
for i in range(n,0,-1):
    if i in l:
        t1=i
        break
while True:
    if t in l:
        t2=t
        break
    else:
        t=t+1
if t1==t2:
    print(0)
else:
    d1=n-t1
    d2=t2-n
    print(min(d1,d2))