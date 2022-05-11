sum=0
while(True):
    num=float(input("Enter a number to stop enter 0:"))
    sum=sum+num
    if num == 0:
        break
print("The sum is ",round(sum,1))