a,b=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    if(l[i]%b!=0):
        c+=1
print(c)