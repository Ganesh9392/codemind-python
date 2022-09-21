def f1(n):
    s=0
    while n:
        p=1
        d=n%10
        n=n//10
        for i in range(1,d+1):
            p=p*i
        s+=p
    return s
n=int(input())
if f1(n)==n:
    print("The number {} is a strong number".format(n))
else:
    print("The number {} is not a strong number".format(n))