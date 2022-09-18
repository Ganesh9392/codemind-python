a,b=map(int,input().split())
t=max(a,b)
for i in range(1,t):
    if a%i==0 and b%i==0:
        r=i
print(r)