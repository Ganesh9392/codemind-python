n=input()
l=list(n.split(" "))
ls=0
ss=0
for i in range(len(l)):
    l2=[]
    s=l[i]
    for j in range(len(s)):
        l2.append(ord(s[j]))
    ls+=max(l2)
    ss+=min(l2)
print(ls-ss)
        