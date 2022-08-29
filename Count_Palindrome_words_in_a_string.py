def fun(s):
    s1=s[::-1]
    if(s1==s):
        return True
    else:
        return False
s=input()
s=s.lower()
l=list(s.split(" "))
c=0
for i in  l:
    if fun(i):
        c+=1
print(c)