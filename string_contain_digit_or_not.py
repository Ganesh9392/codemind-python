n=input()
c=0
t="0123456789"
for i in n:
    if i in t:
        c+=1
if c==0:
    print("Doesn't contain digit")
else:
    print("Contains {} digit".format(c))