def fun(n):
    t=str(n)
    t=t[::-1]
    return n+int(t)
n=int(input())
while True:
    n=fun(n)
    n=str(n)
    if n==n[::-1]:
        print(n)
        break
    else:
        n=int(n)
    