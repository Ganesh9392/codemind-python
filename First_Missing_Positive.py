n=int(input())
l=list(map(int,input().split()))
x=1
while True:
    if x not in l:
        print(x)
        break
    else:
        x+=1