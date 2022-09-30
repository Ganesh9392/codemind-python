def fun(x):
    x=str(x)
    t=x[-1]
    if t=="2" or t=="3" or t=="9":
        return True
    else:
        return False
num=int(input())
for k in range(num):
    c=0
    a,b=map(int,input().split())
    for i in range(a,b+1):
        if fun(i):
            c+=1
    print(c)