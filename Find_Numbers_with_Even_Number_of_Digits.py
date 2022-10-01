n=int(input())
l=list(map(int,input().split()))
#print(l)
c=0
for i in range(len(l)):
    if len(str(l[i]))%2==0:
        c+=1
print(c)