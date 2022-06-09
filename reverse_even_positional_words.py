n=input()
l=n.split(" ")
l=list(l)
for i in range(len(l)):
    if(i%2==0):
        s="".join(reversed(l[i]))
        l[i]=s
print(*l)        