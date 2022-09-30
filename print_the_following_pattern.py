def fun(x):
    x=list(x)
    s=""
    for i in x:
        s+=i
    return s
n=int(input())
s=""
for i in range(n):
    l=[]
    for j in range(n):
        if i==j:
            l.append("0")
        else:
            l.append("x")
    print(fun(l))