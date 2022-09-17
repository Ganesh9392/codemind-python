n=input()
t="0123654789"
s=0
for i in n:
    if i in t:
        s+=int(i)
print(s)