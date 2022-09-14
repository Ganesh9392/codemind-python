def fun(x):
    s=1
    for i in range(1,x+1):
        s=s*i
    return s
for i in range(int(input())):
    a=int(input())
    print(fun(a))