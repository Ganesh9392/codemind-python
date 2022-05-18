num=int(input())
k=0
for j in range(2,num):
    if(num%j==0):
        k=k+1
if(k==0):
    s=0
    c=0
    while num!=0:
        r=num%10
        s=s*10+r
        num=num//10
    for i in range(1,s+1):
        if s%i==0:
            c+=1
    if c==2:
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")
        
    
