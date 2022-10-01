n=int(input())
l=list(map(int,input().split()))
c=l.count(0)
r=[]
for i in range(len(l)):
    if l[i]!=0:
        r.append(l[i])
for i in range(c):
    r.append(0)
print(*r)