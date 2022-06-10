n=input()
n=list(n)
v="ZXCVBNMASDFGHJKLPOIUYTREWQ"
c=0
for i in range(len(n)):
    if(n[i] in v):
        c+=1
print(c)