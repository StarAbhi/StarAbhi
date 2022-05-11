#month name function to get the name by number
def monthName(n):
    month ={1:'January', 2:'February', 3:'March', 
        4:'April', 5:'May', 6:'June', 7:'July',
        8:'August', 9:'September', 10:'October',
        11:'November', 12:'December'}
    return month[n]
#get the first day by month number 
def firstDayOfMonth(n):
    #first day of 2022 months 
    firstDay={1:6,2:2,3:2,4:5,5:0,6:3,7:5,
    8:1,9:4,10:6,11:2,12:4}
    return firstDay[n]
#get the number of days by month number
def daysInMonth(n):
    days ={1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 
     7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    return days[n]
##########(MAIN)###########
#take valid month number from user 
while True:
    month=int(input("Enter the number of a month (1..12): "))
    if month<13 and month>0:
        break
    else:
        print("\tMonth must e between 1 and 12, Try again!")

#call function 
firstDay=firstDayOfMonth(month)
days=daysInMonth(month)
totalDays=firstDay+days
print("   ",monthName(month),2022)
print('Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa')
count=1
#print calendar from data 
for i in range(6):
    if count<days:
        for i in range(7):
            if firstDay>i:
                print("  ",end=" ")
            else:
                print("{:2d}".format(count),end=" ")
                count +=1
            if count>days:
                break
    print()
    firstDay=-1
    
        