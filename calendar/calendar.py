def getMonth():
    try:
        mm=int(input("Enter a month number:"))
        if mm>0 and mm<13:
            return mm
        else:
            print("Month must be between 1 and 12.")
            return getMonth()
    except:
        print("Month must be an integer.")
        return getMonth()

def getYear():
    try:
        yy=int(input("Enter year:"))
        if yy>1752:
            return yy
        else:
            print("Year must be 1753 or later.")
    except:
        print("Year must be an integer.")
        return getYear()
def checkLeap(yy):
    if((yy%400==0)or(yy%100!=0)and(yy%4==0)):
        return True
    else:
        return False
def day_of_week(year,month,day):
    if(month<3):
        month+=12
        year-=1
    result = (day + (int((13*(month-2))/5))+year+(int(year/4))-(int(year/100))-(int(year/400)))%7
    return int(result)+1
  

mm = getMonth()
yy = getYear()
     
# code below for calculation of odd days
day = day_of_week(yy,mm,1)
week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(week_days[day])
notLeapYear =[31, 28, 31, 30, 31, 30, 
      31, 31, 30, 31, 30, 31]
leapYear =[31, 29, 31, 30, 31, 30, 
     31, 31, 30, 31, 30, 31]
s = 0

if checkLeap(yy):
    s=366
else:
    s=365  
  
day += s % 7
day = day % 7
   
# variable used for white space filling 
# where date not present
space =''
space = space.rjust(2, ' ')
  
# code below is to print the calendar
print(mm, yy)
print('Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa')
  
if mm == 9 or mm == 4 or mm == 6 or mm == 11: 
    for i in range(31 + day):
          
        if i<= day:
            print(space, end =' ')
        else:
            print("{:02d}".format(i-day), end =' ')
            if (i + 1)% 7 == 0:
                print()
elif mm == 2:
    if yy % 4 == 0:
        p = 30
    else:
        p = 29
          
    for i in range(p + day):
        if i<= day:
            print(space, end =' ')
        else:
            print("{:02d}".format(i-day), end =' ')
            if (i + 1)% 7 == 0:
                print() 
else:
    for i in range(32 + day):
          
        if i<= day:
            print(space, end =' ')
        else:
            print("{:02d}".format(i-day), end =' ')
            if (i + 1)% 7 == 0:
                print()