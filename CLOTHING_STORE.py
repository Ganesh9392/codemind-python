n=int(input())
l=list(map(int,input().split()))
s=set(l)
r=[]
c=0
for i in s:
    r.append(l.count(i))
for i in r:
    c+=i//2
print(c)