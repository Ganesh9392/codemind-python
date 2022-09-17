n=int(input())
l=list(map(int,input().split()))
oc=0
ec=0
for i in range(len(l)):
    if i%2==0:
        ec+=l[i]
    else:
        oc+=l[i]
if ec==oc:
    print("YES")
else:
    print("NO")