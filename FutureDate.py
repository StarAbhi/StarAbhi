date=input("Enter the current date : ")
day=int(input("Enter a number of  day : "))
list=date.split("/")
d=int(list[0])
m=int(list[1])
y=int(list[2])
d=day+d
while True:
    if d > 30:
        m = int(m+(d/30))
        d=int(d%30)
    elif m>12:
        y=int(y+(m/12))
        m=m%12
    elif d<=30 and m<=12:
        break

futureDate=str(d)+'/'+str(m)+'/'+str(y)
print("In",day,"days, the date will be", futureDate)
    

