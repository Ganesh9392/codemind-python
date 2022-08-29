a,b=map(int,input().split())
l=[]
for _ in range(a):
    l1=[]
    l1=list(map(int,input().split()))
    l.append(l1)
es=0
os=0
for i in l:
    for j in i:
        if j%2==0:
            es+=j
        else:
            os+=j
print(es,os)
