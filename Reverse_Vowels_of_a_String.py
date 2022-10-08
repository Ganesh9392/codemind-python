s=input()
s=list(s)
l=[]
t="aeiouAEIOU"
for i in range(len(s)):
    if s[i] in t:
        l.append(s[i])
        s[i]=" "
l=l[::-1]
t=0
for i in range(len(s)):
    if s[i]==" ":
        s[i]=l[t]
        t+=1
r=""
for i in s:
    r+=i
print(r)
        