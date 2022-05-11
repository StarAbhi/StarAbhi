#get input from user 
num = int(input("Enter the number : "))
#make a count for 2nd 3rd 4th ....
count = num - 1
#for loop to print the sequences
for i in range(num*2,0,-1):
    #if value of i is even then print i else print cube of count
    if i%2==0:
        print(i,end=",")
    else:
        print(count**3,end=",")
        count -=1
