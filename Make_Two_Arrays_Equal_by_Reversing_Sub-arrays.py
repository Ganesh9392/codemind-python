n1=int(input())
l1=list(map(int,input().split()))
n2=int(input())
l2=list(map(int,input().split()))
f=1
for i in range(len(l1)):
    if l1[i] not in l2:
        f=0
        break
for i in range(len(l2)):
    if l2[i] not in l1:
        f=0
        break
if f==0:
    print(False)
else:
    print(True)