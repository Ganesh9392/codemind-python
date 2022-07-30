import math as m
def prime(n):
    if(n<2):
        return False
    for i in range(2,int(m.sqrt(n))+1):
        if(n%i==0):
            return False
    return True
def fib(n):
    n=str(n)
    t=n[::-1]
    if(n==t):
        return True
    return False
n=int(input())
while True:
    n+=1
    if(prime(n) and fib(n)):
        print(n)
        break