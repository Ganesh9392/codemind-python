n,d=map(int,input().split())
l=list(map(int,input().split()))
c=0
r=0
for i in l:
    if i>d:
        c+=1
    elif c==2:
        break
    elif i<=d :
        r+=1
print(r)