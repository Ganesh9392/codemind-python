a,b=map(int,input().split())
if a>b:
    a,b=b,a
i=1
t=b
while True:
    if t%a==0:
        print(t)
        break
    else:
        t=b*i
    i+=1