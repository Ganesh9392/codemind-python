n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)-1):
    t=l[i+1:]
    l1.append(max(t))
l1.append(-1)
print(*l1)