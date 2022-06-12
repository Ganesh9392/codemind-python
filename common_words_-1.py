s1=input()
s1=s1.lower()
s1=list(s1.split())
s2=input()
s2=s2.lower()
s2=list(s2.split(" "))
c=0
for i in range(len(s2)):
    if(s2[i] in s1):
        #if(s2.count(s2[i])==1 and s1.count(s2[i])==1):
        c+=1
print(c)
        