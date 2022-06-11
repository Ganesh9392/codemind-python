n=input()
l=list(n.split(" "))
l2=[]
l3=list(n)
for i in range(len(l)):
    s=l[i]
    for j in range(len(s)):
        l2.append(ord(s[j]))
s=chr(min(l2))
sc=l3.count(s)
l=chr(max(l2))
lc=l3.count(l)
print(s,sc,l,lc)
        