n=int(input())
b=bin(n)
b=b[2:]
s=""
for i in b:
    if i=="0":
        s+="1"
    else:
        s+="0"
r=0
l=len(s)
for i in s:
    l=l-1
    r+=int(i)*2**l
print(r)
    