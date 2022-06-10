n=input()
n=list(n.split(" "))
c=0
v="aeiouAEIOU"
for i in range(len(n)):
    l=list(n[i])
    if(l[0] in v):
        c+=1
print(c)