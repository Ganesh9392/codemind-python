n,r,q=map(int,input().split())
l=list(map(int,input().split()))
p=[]
for i in range(q):
    t=int(input())
    p.append(t)
t=l[len(l)-r:]
l=t+l
#print(l)
#print(p)
for i in p:
    print(l[i])