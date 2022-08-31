s=input()
s1=s.lower()
l3=[]
s1=list(s1.split(" "))
s2=s.upper()
s2=list(s2.split(" "))
l1=list(s1[-1])
l1.sort()
l2=list(s2[-1])
l2.sort()
if l2[0] in s:
    l3.append(l2[0])
if l1[0] in s:
    l3.append(l1[0])
print(l3[-1])
