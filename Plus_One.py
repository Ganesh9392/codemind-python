n=int(input())
l=list(map(str,input().split()))
s=""
for i in l:
    s+=i
s=int(s)
s=s+1
s=str(s)
s=list(s)
print(*s)