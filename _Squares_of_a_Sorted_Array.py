n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    l[i]=l[i]**2
l.sort()
print(*l)