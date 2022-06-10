n=input()
n=list(n)
v="zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP"
c=0
for i in range(len(n)):
    if(n[i]==" "):
        continue
    if(n[i] not in v):
        c+=1
print(c)