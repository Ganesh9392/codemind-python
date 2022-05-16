num=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    if(l[i]%2==0):
        c=c+1
if(c==num):
    print(True)
else:
    print(False)