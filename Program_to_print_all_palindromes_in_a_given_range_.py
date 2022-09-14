a=int(input())
b=int(input())
for i in range(a,b+1):
    i=str(i)
    if i==i[::-1]:
        print(int(i),end=" ")