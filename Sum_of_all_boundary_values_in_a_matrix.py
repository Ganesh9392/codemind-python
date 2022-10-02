r,c=map(int,input().split())
l=[]
for i in range(r):
    t=list(map(int,input().split()))
    l.append(t)
s=0
for i in range(len(l)):
    if i==0 or i==len(l)-1:
        s+=sum(l[i])
    else:
        a=l[i]
        b=a[0]
        c=a[-1]
        s+=c
        s+=b
        
print(s)