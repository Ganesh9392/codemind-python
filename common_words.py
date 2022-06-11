s1=input()
s1=s1.lower()
s1=list(s1.split(" "))
s2=input()
s2=s2.lower()
s2=list(s2.split(" "))
for i in range(len(s2)):
    if(s2[i] in s1):
        print(s2[i],end=" ")
