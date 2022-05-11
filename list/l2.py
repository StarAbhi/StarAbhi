#define a list l1 
l1=list()
#add number in l1 by append method
l1.append(int(input("Enter first number:")))
l1.append(int(input("Enter second number:")))
l1.append(int(input("Enter third number:")))
#print l1
print("The list entered is:",l1)
#sum of first two number by index 
sumOfl1=l1[0]+l1[1]
#print sumOfl1
print("The sum of the first 2 elements =",sumOfl1)
