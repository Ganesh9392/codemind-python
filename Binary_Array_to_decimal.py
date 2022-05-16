num=int(input())
l=list(map(int,input().split()))
r=0
for i in range(len(l)):
    num=num-1
    s=l[i]*2**num
    r=r+s
print(r)