s1=list(map(str,input()))
s2=list(map(str,input()))
for s in range(0,len(s2)):
    k=w=l=0
    w=ord(s1[s])
    l=ord(s2[s])
    k=w+l
    if k>96 and k<123:
        print(chr(k),end="")
    elif (k-96)<122 and(k-96)>96:
        k=k-96
        print(chr(k),end="")
    elif k>148:
        k=k-96-26
        print(chr(k), end="")
    else:
        k=k-26
        print(chr(k), end="")
