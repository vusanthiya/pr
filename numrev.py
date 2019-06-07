numbers=int(input())
rev=0
while(numbers>0):
 rem=numbers%10
 rev=(rev*10)+rem
 numbers=numbers//10
print(rev)
