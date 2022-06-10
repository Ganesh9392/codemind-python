n=input()
n=n.split(" ")
v="aeiou"
v=list(v)
for i in range(len(n)):
    l=list(n[i])
    c=0
    for j in range(len(l)):
        if(l[j] in v):
            c+=1
    print(c,end=" ")
        