n=int(input())
l=list(map(int,input().split()))
t=max(l)
l1=[]
for i in range(1,t+1):
    l1.append(i**2)
s=0
for i in l:
    if i in l1:
        s+=i
print(s)