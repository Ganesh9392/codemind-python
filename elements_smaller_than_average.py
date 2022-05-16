num=int(input())
l=list(map(int,input().split()))
avg=sum(l)//num
c=0
for i in range(len(l)):
    if(l[i]<=avg):
        c=c+1
print(c)