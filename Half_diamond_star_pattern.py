n=int(input())
if n<3:
    print("The pattern is not possible")
else:
    for i in range(1,n+1):
        #print(i,end=" ")
        print(i*"*")
    for j in range(n-1,0,-1):
        #print(j,end=" ")
        print(j*"*")