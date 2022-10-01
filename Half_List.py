n=int(input())
l=list(map(int,input().split()))
l1=l[:len(l)//2]
l2=l[len(l)//2:]
l2=l2[::-1]
print(*(l2+l1))