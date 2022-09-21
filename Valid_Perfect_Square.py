import math
def fun(n):
    t=math.sqrt(n)
    t1=int(t)
    if t==t1:
        return True
    return False
n=int(input())
for i in  range(n):
    num=int(input())
    print(fun(num))
    