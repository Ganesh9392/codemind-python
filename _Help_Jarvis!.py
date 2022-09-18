n=int(input())
for x  in range(n):
    s=int(input())
    s=str(s)
    l=[]
    r=[]
    for t in s:
        l.append(int(t))
    m=min(l)
    mm=max(l)
    for i in range(m,mm+1):
        r.append(i)
    l.sort()
    if l==r:
        print("YES")
    else:
        print("NO")