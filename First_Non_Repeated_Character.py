num=int(input())
for i in range(num):
    n=int(input())
    s=input()
    s=list(s)
    for i in s:
        if s.count(i)==1:
            print(i)
            break
    else:
        print(-1)