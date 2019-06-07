str1=input()
str1=list(str1)
if str1==str1[::-1]:
	while str1==str1[::-1]:
		str1[-1]=""
h=""
for i in str1:
	h=h+i
print(h)
