n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
l3=[]
l4=[]
for i in range(len(l)):
    if(l[i]%2==0):
        l1.append(l[i])
    else:
        l2.append(l[i])
if(len(l1)==len(l2)):
    for i in range(len(l2)):
        l3.append(l2[i])
        l3.append(l1[i])
    print(*l3)
else:
    if(len(l1)>len(l2)):
        for i in range(len(l1)):
            l2.append("*")
            if(len(l1)==len(l2)):
                break
        for i in range(len(l1)):
            l3.append(l2[i])
            l3.append(l1[i])
    elif(len(l1)<len(l2)):
        for i in range(len(l2)):
            l1.append("*")
            if(len(l1)==len(l2)):
                break
        for i in range(len(l1)):
            l3.append(l2[i])
            l3.append(l1[i])
    for i in range(len(l3)):
        if(l3[i]=="*"):
            continue
        else:
            l4.append(l3[i])
    if(len(l4)%2==1):
        l4.append(0)
    print(*l4)