string=input()
substring=""
a=0
op=[]
if string==string[::-1]:
  op.append(0)
for y in range(len(string)-1):
  for z in range(y+1,len(string)):
    substring=string[y:z+1]
    if substring==substring[::-1]:
      op.append(len(string)-len(substring))
     
print(min(op))
