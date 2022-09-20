n=int(input())
if n<0:
    t=-1
else:
    t=1
n=abs(n)
n=str(n)
n=n[::-1]
n=int(n)
print(t*n)