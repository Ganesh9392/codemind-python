n,t=map(int,input().split())
l=list(map(int,input().split()))
for i in range(t):
    l.append(l[i])
print(*l[t:])
