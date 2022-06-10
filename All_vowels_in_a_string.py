s=input()
s=list(s)
v="aeiou"
v=list(v)
l=[]
for i in range(len(s)):
    if(s[i] in v):
        l.append(s[i])
m=set(l)
l=list(m)
l.sort()
if(l==v):
    print(True)
else:
    print(False)