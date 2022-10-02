def fun(l):
    t=l[::-1]
    t.sort()
    if l==t or l==t[::-1]:
        return True
    return False
r,c=map(int,input().split())
l1=[]
l2=[]
for i in range(r):
    t=list(map(int,input().split()))
    l1.append(t)
r=0
for i in l1:
    if fun(i):
        r+=1
print(r)