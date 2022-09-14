import math
def fun(n):
    if n==1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
a=int(input())
b=int(input())
c=a+b
t=c
while True:
    c=c+1
    if fun(c):
        break
print(c-t)