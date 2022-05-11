#Print Table by using nested looping 
n=int(input("Enter the Range "))
for i in range(2,n+1):
    print("Table of : ",i)
    for j in range(1,11):
        print(i," X ",j," = ",i*j)

#find the factorial of  a given number from user 
fact=1
while(n>0):
    if(n>1):
        fact=fact*n
        n -=1
    else:
        n -=1 
        
print("Factorial : ",fact)