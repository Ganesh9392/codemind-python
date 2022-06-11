n=input()
n=list(n)
l=[]
for i in range(len(n)):
    if(n.count(n[i])==1):
        if(ord(n[i])>ord("Z")):
            l.append(n[i])
l.sort()
for i in range(len(l)):
    print(l[i],end="")
        