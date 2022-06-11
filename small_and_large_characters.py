n=input()
l=list(n.split(" "))
for i in range(len(l)):
    s=l[i]
    l2=[]
    for j in range(len(s)):
        l2.append(ord(s[j]))
    print(chr(min(l2)),chr(max(l2)),end=" ")
        
