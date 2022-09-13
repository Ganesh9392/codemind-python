import math
def fun(x):
    c=0
    if x==1:
        return False
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True
a=int(input())
b=int(input())
c=0
for j in range(a,b+1):
    if fun(j):
        #print(j,end=" ")
        c+=1
print(c)