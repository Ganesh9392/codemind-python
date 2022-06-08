n=input()
n=n.split(" ")
l=list(n)
l1=[]
for i in range(len(l)):
    l1.append(len(l[i]))
print(max(l1))