s1=input()
s1=s1.lower()
s1=list(s1)
s2=input()
s2=s2.lower()
s2=list(s2)
r=""
c=0
for i in range(len(s2)):
    if(s2[i] in s1):
        if(s2[i]!=" "):
            r=r+s2[i]
            c+=1
if(c==0):
    print(-1)
else:
    r=set(r)
    r=list(r)
    r.sort()
    for i in range(len(r)):
        print(r[i],end="")