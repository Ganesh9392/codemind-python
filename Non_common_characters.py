s1=input()
s1=s1.lower()
s1=list(s1)
s2=input()
s2=s2.lower()
s2=list(s2)
l=[]
for i in range(len(s2)):
    if(s2[i] not in s1):
        if(s2[i] not in l):
            if(s2[i]!=" "):
                l.append(s2[i])
for j in range(len(s1)):
    if(s1[j]  not in s2):
        if(s1[j] not in l):
            if(s1[j]!=" "):
                l.append(s1[j])
print(len(l))
