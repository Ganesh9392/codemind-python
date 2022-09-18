n=int(input())
l=list(map(int,input().split()))
l=set(l)
l=list(l)
l.sort()
if len(l)<3:
    print(max(l))
else:
    print(l[-3])