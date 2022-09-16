d="1023456789"
for _ in range(int(input())):
    s=input()
    for i in s:
        if i in d:
            print("Yes")
            break
    else:
        print("No")
    