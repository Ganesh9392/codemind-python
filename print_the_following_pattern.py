n=int(input())
l="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
l=list(l)
for i in range(n,0,-1):
    for _ in range(i):
        print(l[i-1],end=" ")
    print()
