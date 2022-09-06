for _ in range(int(input())):
    n=input()
    r=0
    l=len(n)
    for i in n:
        l=l-1
        r+=int(i)*2**l
    print(r)