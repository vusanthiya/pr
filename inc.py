string=int(input())
li=list(map(int,input().split()))
sorting=sorted(l)
li1=[]
for i in range(0,len(li)):
    for j in range(0,len(li)):
        if li[i]==sorting[j]:
            li1.append(j)
            
for i in range(len(l1)):
	li1[i]=li1[i]+1
print(*li1)
