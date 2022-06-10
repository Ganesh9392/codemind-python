n=input()
n=n.split(" ")
v="aeiou"
v=list(v)
l1=[]
for i in range(len(n)):
    l=list(n[i])
    c=0
    for j in range(len(l)):
        if(l[j] in v):
            c+=1
    l1.append(c)
print(min(l1))
        