#asks user for 10 integers
print("Enter 10 integers")
#make a empty list of numbers
numbers=[]
#get 10 integers from user
for i in range(10):
    num=int(input())
    numbers.append(num)
#print the user given integers
print("Before Selection Sort : ",numbers)
#traverse the numbers 
for n in range(10):
    #let minimum value index in numbers is n
    #assign in min variabel
    min=n
    #now check min with other index if any 
    #index value is less then min so store in min 
    for m in range(n+1,10):
        if numbers[min]>numbers[m]:
            min = m
    #after this swap the n index value with min index value
    numbers[n],numbers[min]=numbers[min],numbers[n]
#print the numbers
print("After Selection Sort : ",numbers)
    
