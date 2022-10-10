n=int(input())
l=list(map(int,input().split()))
e=int(input())
t=max(l)
for i in l:
    if (e+i)>=t:
        print(True,end=" ")
    else:
        print(False,end=" ")