#prompts user to enter the month and day
month=int(input("Enter the month (1 to 12 ): "))
day=int(input("Enter the day : "))
#check the month and day and assign season 
if month >0 and month<4:
    season = "Winter"
elif  month >3 and month<7:
    season = "Spring"
elif month>6 and month <10:
    season = "Summer"
elif month>12:
    season = "Fall"
if month%3==0 and day>=21:
    if season=="Winter":
        season="Spring"
    elif season=="Spring":
        season="Summer"
    elif season=="Summer":
        season="Fall"
    else:
        season="Winter"
#print the season 
print("Season : ",season)