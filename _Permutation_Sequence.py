import itertools
n,k=map(int,input().split())
l=[]
for i in  range(1,n+1):
    l.append(i)
t=itertools.permutations(l)
c=0
for i in (t):
    c+=1
    if c==k:
        r=i
        break
for i in r:
    print(i,end="")
