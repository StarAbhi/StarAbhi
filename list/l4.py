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
#create a new list 
l2=list()
#append first and last number from l1 in l2
l2.append(l1[0])
l2.append(l1[-1])
#print l2 
print("The new list is:",l2)
#calculate sum of l1 and l2 by sum() function 
sumofl1l2=sum(l1)+sum(l2)
#print sum
print("The sum of both list = ",sumofl1l2)
