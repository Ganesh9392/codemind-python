num=int(input())
l=list(map(int,input().split()))
big=max(l)
if(big==1 or big==0):
    print(True)
else:
    print(False)