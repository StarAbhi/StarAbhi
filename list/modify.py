#initializes a modList 
modList=[0,2,-4,5,6,0,7,9,-3,0]
#define a zero=0 variable this hold the number of zero in list  
zero=0
#use for loop to check all the element of list and replace -ve value with 0
#also count number of  zero
for i in range(len(modList)):
    if modList[i]==0:
        zero +=1
    elif modList[i]<0:
        modList[i]=0
    else:
        pass
#print details 
print("There were",zero,"zeroes in the original list")
print("The new list is ",modList)