#this function use to get valid month from user 
def getMonth():
    month=int(input("Enter a Month in numeric form ( 1 to 12): "))
    if month>=1 and month<=12:
        return month
    else:
        print("Invalid Month !! Try Again !!")
        return getMonth()
#this function use to get valid day from user
def getDay():
    day=int(input("Enter  Day in numeric form ( 1 to 31): "))
    if day>=1 and day<=31:
        return day
    else:
        print("Invalid Day !! Try Again !!")
        return getDay()
#this function use to get valid year from user
def getYear():
    year=int(input("Enter  Year in numeric form ( 0 to 99): "))
    if year>=0 and year<=99:
        return year
    else:
        print("Invalid Year !! Try Again !!")
        return getYear()


def main():
    #call the function to get input from user 
    month=getMonth()
    day=getDay()
    year=getYear()
    #print user given date 
    print("The date is {}/{}/{}".format(month,day,year))
    #print the result accoding to the condition ..
    if month*day==year:
        print("This is a magic date.")
    else:
        print("This is not a magic date.")
main()
