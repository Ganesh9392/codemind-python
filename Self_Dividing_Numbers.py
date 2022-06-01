a=int(input())
b=int(input())
for i in range(a,b+1):
    if(i%10==0):
        continue
    t=i
    c=0
    while i:
        d=i%10
        if(d==0):
            continue
        if(t%d==0):
            c+=1
        i=i//10
        if(c==len(str(t))):
            print(t,end=" ")
        
