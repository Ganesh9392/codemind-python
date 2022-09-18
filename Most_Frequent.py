n=int(input())
l=list(map(int,input().split()))
s=set(l)
s=list(s)
m=0
c=0
for i in  range(len(s)):
    if l.count(s[i])>m:
        m=l.count(s[i])
        t=s[i]
print(t)