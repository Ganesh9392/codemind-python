n=input()
n=list(n)
v="aeiouAEIOU"
v=list(v)
l=[]
c=0
for i in range(len(n)):
    if(n[i] in v):
        if(n[i] not in l):
            l.append(n[i])
            c+=1
if(c==0):
    print(-1)
else:
    print(*l)
