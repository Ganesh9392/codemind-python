n=int(input())
l=[]
for i in range(n):
    s=input()
    if s=="++X" or s=="X++":
        l.append(1)
    elif s=="--X" or s=="X--":
        l.append(-1)
print(sum(l))