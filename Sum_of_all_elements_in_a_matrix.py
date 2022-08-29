a,b=map(int,input().split())
l=[]
for _ in range(a):
    l1=[]
    l1=list(map(int,input().split()))
    l.append(l1)
s=0
for i in l:
    for j in i:
        s+=j
print(s)