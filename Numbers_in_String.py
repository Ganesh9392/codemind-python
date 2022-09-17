n=input()
s=0
t="0123456789"
for i in n:
    if i in t:
        s+=int(i)
print(s)