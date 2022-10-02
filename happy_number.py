def fun(n):
    s=0
    while n:
        d=n%10
        n=n//10
        s+=d**2
    return s
n=int(input())
while True:
    n=fun(n)
    if n<10:
        t=n
        break
if t==1 or t==7:
    print(True)
else:
    print(False)