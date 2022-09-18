n=int(input())
l=list(map(int,input().split()))
n=n//2
l1=[]
l2=[]
for i in range(n):
    l1.append(l[i])
    l2.append(l[i+n])
for i in range(len(l1)):
    print(l1[i],l2[i],end=" ")
