num=int(input())
l=list(map(int,input().split()))
if(len(l)%2==1):
    l.append(0)
for i in range(len(l)):
    print(l[i],end=" ")