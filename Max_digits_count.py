num=int(input())
l=list(map(str,input().split()))
ml=1
l1=[]
for i in range(len(l)):
    if(len(l[i])>ml):
        ml=len(l[i])
for j in range(len(l)):
    if(len(l[j])==ml):
        l1.append(l[j])
print(len(l1))