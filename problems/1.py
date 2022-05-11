#define num
numbers=[]
size=1
print("Enter 5 numbers")
#get number form user
while(size<=5):
    num=int(input())
    numbers.append(num)
    size +=1
size=0
#print number and its cube
while(size<5):
    print("Number {} its Cobe {}.".format(numbers[size],numbers[size]**3))
    size +=1
