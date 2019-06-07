def convert(n): 
    if(len(n) == 0): 
        return
    n1 = '' 
    n1 +=n[0].upper() 
    for i in range(1, len(n) - 1): 
        if (n[i] == ' '): 
            n1 += n[i + 1].upper() 
            i += 1
        elif(n[i - 1] != ' '): 
            n1 += n[i]  
    print(n1)      
              
  
 
def main(): 
    n = input()
    convert(n) 
      
if __name__=="__main__": 
    main()  
      
