h,m=map(int,input().split(":"))
a=30*h-11/2*m
if a<0:
    a=a*-1
t=a
k=abs(t-360)
if t<k:
    print(t)
else:
    print(k)