n1=int(input())
l1=list(map(int,input().split()))
n2=int(input())
l2=list(map(int,input().split()))
num=int(input())
c=0
for i in range(len(l1)):
    for j in range(l1[i],l2[i]+1):
        if j==num:
            c+=1
print(c)