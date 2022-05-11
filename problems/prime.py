### DO NOT MODIFY ###
num = int(input("Enter integer greater than 1:"))
print()
### DO NOT MODIFY ###

# YOUR CODE HERE

flag=1
for i in range(2,int(num**0.5)+1): # range[2,sqrt(num)]
    if(num%i==0):
        flag=0
        print("Not Prime")
        break
    
if flag==1:
    print("Prime")
        
