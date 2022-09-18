n,x=map(int,input().split())
for i in range(1,x+1):
    if i%2==0:
        continue
    else:
        print("{} x {} = {}".format(n,i,n*i))