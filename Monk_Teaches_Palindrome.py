n=int(input())
for i in range(n):
    t=""
    s=input()
    if len(s)%2==0:
        t="EVEN"
    else:
        t="ODD"
    if s==s[::-1]:
        print("YES",t)
    else:
        print("NO")