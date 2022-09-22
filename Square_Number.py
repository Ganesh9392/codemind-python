def fun(l,n):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]+l[j]==n:
                return True
    return False
n=int(input())
l=[]
for i in range(n+1):
    l.append(i**2)
print(fun(l,n))
