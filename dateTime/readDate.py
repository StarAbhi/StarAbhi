from datetime import date, datetime, timedelta,time
def read_date():
    inputDate=input()
    listDate=inputDate.split("-")
    x = date(int(listDate[0]),int(listDate[1]),int(listDate[2]))
    return x

DateObject=[]
print("Input : ")
for i in range(4):
    DateObject.append(read_date())

DateObject.sort()
print("Output : ")
for i in DateObject:
    print(i.strftime("%m/%d/%Y"))
print((DateObject[3]-DateObject[2]).days)
d = timedelta(days=21)
t= DateObject[-1]+d
print(t.strftime("%B %d, %Y"))
print(DateObject[0].strftime("%A"))