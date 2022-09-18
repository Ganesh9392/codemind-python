n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l=l1+l2
    l.sort()
    print(*l)