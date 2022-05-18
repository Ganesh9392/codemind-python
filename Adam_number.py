num=int(input())
r1=num**2
num1=0
r=0
while num:
    d=num%10
    num1=num1*10+d
    num=num//10
r2=num1**2
while r2:
    d1=r2%10
    r=r*10+d1
    r2=r2//10
if(r==r1):
    print(True)
else:
    print(False)
    
    