import math 
def fun(n):
    if n==1:
        return True
    for i in  range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
l=[]
t1=0
t2=0
n=int(input())
for i in range(n):
    if fun(i):
        l.append(i)
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]*l[j]==n:
            t1=l[i]
            t2=l[j]
            break
if t1==0 and t2==0:
    print(-1)
else:
    print(t1,t2)
        