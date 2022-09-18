n=int(input())
l="ZXCVBNMLKJHGFDSAQWERTYUIOP"
l=list(l)
l.sort()
for i in range(n):
    for _ in range(n):
        print(l[i],end=" ")
    print()
        