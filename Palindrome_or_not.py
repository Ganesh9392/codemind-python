s=input()
s=s.lower()
r=""
for i in s:
    r=i+r
if(r==s):
    print(True)
else:
    print(False)