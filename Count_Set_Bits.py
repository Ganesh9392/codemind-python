for _ in  range(int(input())):
    n=input()
    t=bin(int(n))
    t=list(t)
    print(t.count("1"))