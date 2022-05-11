#name a empty list of numbers to store numbers 
numbers = []
#take five input from user by using for loop 
print("Enter five numbers : ")
for i in range(1,6):
    n=int(input(f"Enter {i} number : "))
    numbers.append(n)

#print all even numbers 
print("Even Numbers : ",end=" ")
#check all numbers one by one and print if number is even 
for num in numbers:
    if num%2==0:
        print(num,end=" ")