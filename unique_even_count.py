num=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
    if(l[i] in l1):
        continue
    if(l[i]%2==0):
        l1.append(l[i])
print(len(l1))