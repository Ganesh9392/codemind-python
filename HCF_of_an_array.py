num=int(input())
l=list(map(int,input().split()))
n=max(l)
t=[]
for i in range(1,n+1):
    c=0
    for j in l:
        if j%i==0:
            c+=1
    if c==len(l):
        t.append(i)
print(max(t))