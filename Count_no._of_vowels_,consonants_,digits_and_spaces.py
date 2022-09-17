s=input()
s=list(s)
v="aeiou"
n="0123456789"
vc=0
cc=0
nc=0
sc=0
for i in s:
    if i in v:
        vc+=1
    elif i in n:
        nc+=1
    elif i==" ":
        sc+=1
    else:
        cc+=1
print("Vowels:",vc)
print("Consonants:",cc)
print("Digits:",nc)
print("White spaces:",sc)