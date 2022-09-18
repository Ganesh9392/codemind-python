a=int(input())
b=int(input())
l=[]
for i in range(a):
    t=list(map(int,input().split()))
    l.append(t)
s=0
for i in l:
    s+=sum(i)
print(s)
    