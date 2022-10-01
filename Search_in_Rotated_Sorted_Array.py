n=int(input())
l=list(map(int,input().split()))
x=int(input())
if x not in l:
    print(-1)
else:
    print(l.index(x))