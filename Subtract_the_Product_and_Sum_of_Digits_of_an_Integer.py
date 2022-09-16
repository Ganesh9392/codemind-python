n=input()
l=[]
for i in n:
    l.append(int(i))
p=1
s=sum(l)
for i in l:
    p=p*i
print(p-s)