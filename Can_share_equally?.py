n,m=map(int,input().split())
a=n*1
b=m*2
if m%2==1 and n==0:
    print("NO")
else:
    if(a+b)%2==0:
        print("YES")
    else:
        print("NO")