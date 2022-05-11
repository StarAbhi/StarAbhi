#get input from user  and store in num 
num = int(input())
#get value of x from user 
x = int(input())
#not we have to divide by x three times 
#so we use for loop and run for loop for 3 times 
#inside for loop we print the number by dividing by x 
#and then update the value of num 
for i in range(3):
    #we use end = " " to print result in same line with space 
    print(num//x,end=" ")
    #update the value of num
    num = num//x