n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    if l.count(i)==1:
        r.append(i)
if len(r)==0:
    print(-1)
else:
    print(max(r))