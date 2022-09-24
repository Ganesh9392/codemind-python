import math
def fun(n):
    if n==0:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
num=int(input())
l=[]
t1=0
t2=0
for i in range(1,num):
    if  fun(i):
        l.append(i)
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]*l[j]==num:
            t1=l[i]
            t2=l[j]
if t1==0 and t2==0:
    print(-1)
else:
    print(t1,t2)
            