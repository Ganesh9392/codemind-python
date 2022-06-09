n=input()
l=list(n.split(" "))
ln=len(l)
while ln:
    ln-=1
    print("".join(reversed(l[ln])),end=" ")