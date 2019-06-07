str=input()
x=[]
for y in str:
	if y not in x:
		x.append(y)
	else:
		break
print(len(x))
