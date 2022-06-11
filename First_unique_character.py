n=input()
n=list(n)
l=[]
c=0
for i in range(len(n)):
    if(n.count(n[i])==1):
        if (n[i])!=" ":
            l.append(n[i])
            c+=1
if(c==0):
    print(-1)
else:
    print(l[0])
        