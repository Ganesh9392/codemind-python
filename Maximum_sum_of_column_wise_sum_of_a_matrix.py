a,b=map(int,input().split())
l=[]
for i in range(a):
    l1=list(map(int,input().split()))
    l.append(l1)
r=[]
for i in range(b):
    cs=0
    for j in range(a):
        cs+=l[j][i]
    r.append(cs)
print(max(r))
    