def fun(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                return False
    return True
num=int(input())
for i in range(num):
    n=int(input())
    l=list(map(int,input().split()))
    if fun(l):
        print(0)
    else:
        print(max(l)-min(l))
    