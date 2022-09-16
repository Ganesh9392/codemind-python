num=input()
num=list(num)
for i in range(len(num)):
    if num[i]=="6":
        num[i]="9"
        break
for i in num:
    print(i,end="")