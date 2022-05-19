num=int(input())
l=list(map(int,input().split()))
l1=[]
c=0
for j in range(len(l)):
    l1.append(l[j])
l1.append(l[0])
for i in range(1,len(l1)-1):
    if(l1[i-1]%2==0 and l1[i+1]%2==1):
        c+=1
print(c*2)