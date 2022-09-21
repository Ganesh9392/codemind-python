def fun(n):
    s=0
    while n:
        d=n%10
        n=n//10
        s+=d
    return s
n=int(input())
#print(n)
while True:
    n=fun(n)
    if n<10:
        print(n)
        break
        
    
    