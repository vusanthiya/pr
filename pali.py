a=input()
j=len(a)-1
b=0
while(1):
  if a[j]=="0":
    b+=1
    j-=1
  else:
    break
if a==a[::-1]:
  print("yes")
else:
  a="0"*b+a
  if a==a[::-1]:
    print("yes")
  else:
    print("no")
