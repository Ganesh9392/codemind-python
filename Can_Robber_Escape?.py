n=int(input())
l=list(map(int,input().split()))
if max(l)>=n:
    print("NO")
else:
    print("YES")