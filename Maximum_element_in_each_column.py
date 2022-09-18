a,b=map(int,input().split())
l=[]
for i in range(a):
    t=list(map(int,input().split()))
    l.append(t)
for i in range(len(l)):
    r=[]
    for j in range(len(l)):
        r.append(l[j][i])
    print(max(r))
        