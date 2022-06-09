n=input()
l=list(n.split(" "))
for i in range(len(l)):
    print("".join(reversed(l[i])),end=" ")