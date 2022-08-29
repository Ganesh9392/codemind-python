a,b=map(int,input().split())
l=[]
for i in range(a):
    l1=list(map(int,input().split()))
    l.append(l1)
rs=0
cs=0
r=[]
for i in l:
    r.append(sum(i))
for i in range(len(l)):
    cs=0
    for j in range(len(l)):
        cs+=l[j][i]
    r.append(cs)
print(max(r))
    