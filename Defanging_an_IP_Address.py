n=input()
n=list(n)
for i in range(len(n)):
    if n[i]==".":
        n[i]="[.]"
for i in n:
    print(i,end="")