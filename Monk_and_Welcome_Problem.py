n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
for i in range(len(l1)):
    print(l1[i]+l2[i],end=" ")