n=int(input())
l=list(map(int,input().split()))
m=set(l)
l1=list(m)
l1.sort()
if(l==l1):
    print("yes")
else:
    print("no")
