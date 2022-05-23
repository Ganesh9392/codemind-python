num=int(input())
l=list(map(int,input().split()))
n1=num//2
l1=[]
l2=[]
for i in range(n1):
    l1.append(l[i])
for j in range(n1,num):
    l2.append(l[j])
print(sum(l2)-sum(l1))