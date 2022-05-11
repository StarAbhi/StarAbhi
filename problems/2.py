#make a infinite loop to get valid input 
#if input is valid break the loop.
while True:
    num=int(input("Enter value between 0 and 100 "))
    #check condition for valid input
    if(num>=1 and num<=100):
        print("Valid Input .")
        break
    else:
        print("Invalid Input !!Try Again Plz !!")

