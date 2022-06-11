n=input()
n=list(n)
l=[]
c=0
for i in range(len(n)):
    if n[i]!=" ":
        if(n[i] not in l):
            if(n[i]>"Z"):
                l.append(n[i])
print(len(l))
        