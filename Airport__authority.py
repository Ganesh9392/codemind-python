n=int(input())
l=[]
for i in range(n):
    t=int(input())
    l.append(t)
s=0
t=int(input())
for i in l:
    if i>t:
        s+=2
    else:
        s+=1
print(s)