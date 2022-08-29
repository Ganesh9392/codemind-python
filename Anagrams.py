def fun(s1,s2):
    for i in s1:
        if i not in s2:
            return False
    return True
s1=input()
s1=s1.lower()
s1=list(s1)
s2=input()
s2=s2.lower()
s2=list(s2)
print(fun(s1,s2))