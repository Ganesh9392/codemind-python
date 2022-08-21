n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    if(l[i]%2==1):
        continue
    elif(i%2==0):
        continue
    else:
        c+=1
if(c==1):
    print(False)
else:
    print(True)