#store 4 in num 
num = 4
#for loop to get 1 to 9 numbers
for i in range(1,10):
    #check the condition for odd number  
    if i%2!=0:
        #print the multiplication table of multiple of 4 
        print("{} X {} = {}".format(num,i,i*num))
