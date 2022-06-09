n=input()
n=list(n)
v="aeiou"
v=list(v)
l=[]
l1=[]
c=0
for i in range(len(n)):
    if(n[i] in v):
        if(n[i] not in l):
            l.append(n[i])
            l.sort()
if(v==l):
    print(0)
else:
    for j in range(len(v)):
        if(v[j] not in l):
            l1.append(v[j])
    print(*l1)
