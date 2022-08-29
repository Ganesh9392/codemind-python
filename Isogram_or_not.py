def fun(s):
    for i in s:
        if s.count(i)>1:
            return False
    return True
s=input()
l=[]
for i in s:
    if i==" ":
        continue
    else:
        l.append(i)
print(fun(l))