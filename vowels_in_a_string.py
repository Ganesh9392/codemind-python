n=input()
n=list(n)
s=input()
c=0
for i in range(len(n)):
    if(n[i]==s):
        c+=1
        r=i
        break
    
if(c==0):
    print(False)
else:
    print(True)
    print(r)