num=int(input())
l=[]
for i in range(num):
    n=int(input())
    l.append(n)
w=int(input())
s=0
for i in l:
    if i>w:
        s+=2
    else:
        s+=1
print(s)