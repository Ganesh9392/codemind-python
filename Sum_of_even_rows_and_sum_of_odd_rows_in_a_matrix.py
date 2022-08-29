a,b=map(int,input().split())
l=[]
for _ in range(a):
    l1=[]
    l1=list(map(int,input().split()))
    l.append(l1)
es=0
os=0
for i in range(len(l)):
    if i%2==0:
        es+=sum(l[i])
    else:
        os+=sum(l[i])
print(es,os)
