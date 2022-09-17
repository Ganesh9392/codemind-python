def fun(n):
    n=str(n)
    t="0123456789"
    for i in n:
        if i not in t:
            return False
    return True
n=int(input())
for i in range(n):
    s=input()
    print(fun(s))