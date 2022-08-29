a,b=map(int,input().split())
l=[]
for i in range(a):
    l1=list(map(int,input().split()))
    l.append(l1)
r=[]
for i in l:
    r.append(sum(i))
print(*r)